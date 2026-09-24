"""The facade against a fake transport: what goes on the wire, what comes back."""

import datetime as dt
import json

import httpx
import pytest

from mentio import AsyncMentio, Mentio, MentioError
from mentio.models import CreateKeywordBody, CreateKeywordBodyKind


def make_client(handler, *, async_=False):
    transport = httpx.MockTransport(handler)
    cls = AsyncMentio if async_ else Mentio
    return cls("mk_live_test", base_url="https://api.test/", httpx_args={"transport": transport})


def json_response(status: int, payload) -> httpx.Response:
    return httpx.Response(status, json=payload, headers={"content-type": "application/json"})


MENTION = {
    "id": "mm_1",
    "status": "open",
    "relevant": True,
    "delivered": False,
    "priority": 61.5,
    "keyword": {"id": "kw_1", "term": "acme"},
    "post": {"platform": "reddit", "url": "https://r/1", "text": "hi", "links": [], "engagement": None, "publishedAt": "2026-09-03T08:12:44.000Z", "replyTo": None},
    "author": None,
    "classification": None,
    "triage": {"assignee": None, "snoozedUntil": None, "note": None},
    "createdAt": "2026-09-03T08:15:02.113Z",
}


def test_search_sends_the_key_and_coerces_strings_into_the_typed_query():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["auth"] = request.headers.get("authorization")
        return json_response(200, {"data": [MENTION], "nextCursor": None})

    client = make_client(handler)
    page = client.mentions.search(platform="reddit", relevant=True, since="2026-09-01T00:00:00Z", limit=5)
    assert seen["auth"] == "Bearer mk_live_test"
    url = httpx.URL(seen["url"])
    assert url.path == "/v1/mentions"
    assert url.params["platform"] == "reddit"
    assert url.params["relevant"] == "true"
    assert url.params["since"].startswith("2026-09-01T00:00:00")
    assert url.params["limit"] == "5"
    assert page.data[0].id == "mm_1"
    assert page.data[0].post.platform.value == "reddit"


def test_instants_accept_datetimes_dates_and_epoch_milliseconds():
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(httpx.URL(str(request.url)).params["since"])
        return json_response(200, {"data": [], "nextCursor": None})

    client = make_client(handler)
    client.mentions.search(since=dt.datetime(2026, 9, 1, tzinfo=dt.timezone.utc))
    client.mentions.search(since=dt.date(2026, 9, 1))
    client.mentions.search(since=1788220800000)
    assert all(s.startswith("2026-09-01T00:00:00") for s in seen), seen


def test_bodies_take_fields_a_dict_or_a_model():
    bodies = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(json.loads(request.content))
        return json_response(201, {"id": "kw_1", "term": "acme", "kind": "brand", "muted": False, "pausedForBalance": False, "pausedForCap": False, "cap": None, "platforms": None, "context": None, "matching": {"requiredTerms": [], "requiredMode": "any", "excludedTerms": [], "excludedAuthors": [], "caseSensitive": False}, "stats": {"mentions": 0, "relevant": 0, "last7d": 0, "thisMonth": 0, "lastMentionAt": None, "feedback": {"relevant": 0, "notRelevant": 0}, "noise": {"scored": 0, "relevant": 0, "noisy": False}}, "polling": [], "createdAt": "2026-09-03T10:04:44.881Z"})

    client = make_client(handler)
    created = client.keywords.create(term="acme", kind="brand")
    client.keywords.create({"term": "acme", "kind": "competitor"})
    client.keywords.create(CreateKeywordBody(term="acme", kind=CreateKeywordBodyKind.TOPIC))
    assert created.id == "kw_1"
    assert [b["kind"] for b in bodies] == ["brand", "competitor", "topic"]


def test_a_union_body_picks_the_variant_by_kind():
    bodies = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(json.loads(request.content))
        return json_response(201, {"id": "dest_1", "kind": "webhook", "label": "Production", "config": {"url": "https://example.com/hook", "headers": {}, "secret": "whsec_x"}, "stats": {"alerts": 0, "activeAlerts": 0, "lastDeliveryAt": None, "last7d": {"total": 0, "failed": 0}}, "createdAt": "2026-09-03T10:04:44.881Z"})

    client = make_client(handler)
    channel = client.channels.create(kind="webhook", url="https://example.com/hook", label="Production")
    assert bodies[0] == {"kind": "webhook", "url": "https://example.com/hook", "label": "Production"}
    assert channel.config.secret == "whsec_x"
    with pytest.raises(ValueError):
        client.channels.create(kind="pigeon")


def test_path_ids_are_positional_and_204_returns_none():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        if request.method == "PATCH":
            return json_response(200, {**MENTION, "status": "done"})
        return httpx.Response(204)

    client = make_client(handler)
    updated = client.mentions.update("mm_1", status="done")
    assert (seen["method"], seen["path"]) == ("PATCH", "/v1/mentions/mm_1")
    assert updated.status.value == "done"
    assert client.keywords.delete("kw_1") is None
    assert (seen["method"], seen["path"]) == ("DELETE", "/v1/keywords/kw_1")


def test_errors_carry_the_api_code_and_message():
    def handler(request: httpx.Request) -> httpx.Response:
        return json_response(401, {"error": {"code": "unauthorized", "message": "Invalid API key"}})

    client = make_client(handler)
    with pytest.raises(MentioError) as raised:
        client.keywords.list()
    assert (raised.value.status, raised.value.code, raised.value.message) == (401, "unauthorized", "Invalid API key")


def test_csv_exports_come_back_as_text():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, text="id,platform\r\nmm_1,x\r\n", headers={"content-type": "text/csv; charset=utf-8"})

    client = make_client(handler)
    assert client.mentions.export(platform="x").startswith("id,platform")


async def test_the_async_client_mirrors_the_sync_one():
    def handler(request: httpx.Request) -> httpx.Response:
        assert httpx.URL(str(request.url)).params["range"] == "7d"
        return json_response(200, {
            "window": {"from": "2026-08-27", "to": "2026-09-02", "days": 7, "timezone": "UTC"},
            "matched": 7, "relevant": 5, "posts": 6, "people": 3,
            "sentiment": {"positive": 3, "neutral": 2, "negative": 1, "unclassified": 1},
            "buyIntent": 1, "questions": 1, "reach": {"followers": 1200, "people": 1},
            "triage": {"open": 5, "ignored": 0, "done": 2, "waiting": 1, "handledRate": 0.4, "medianTimeToDoneMs": 14400000},
            "previous": None,
        })

    async with make_client(handler, async_=True) as client:
        summary = await client.analytics.summary(range_="7d", compare=False)
    assert summary.matched == 7
    assert summary.window.timezone == "UTC"
