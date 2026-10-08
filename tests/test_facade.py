"""The facade against a fake transport: what goes on the wire, what comes back."""

import datetime as dt
import json
import pathlib

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


# The API's own description of its responses. The sample mention and keyword
# below are BUILT from it: every field the API marks required is filled with
# a minimal value of its type, and a test names only the values it reads.
# Hand-written samples broke the release each time a response gained a
# required field (feeds, comments, cross-posts: four failed releases in a
# row on 2026-10-07), with nothing to say so before the merge.
SPEC = json.loads((pathlib.Path(__file__).parent.parent.parent / "sdk" / "openapi.json").read_text())
SCHEMAS = SPEC["components"]["schemas"]


def _resolve(schema: dict) -> dict:
    while "$ref" in schema:
        schema = SCHEMAS[schema["$ref"].rsplit("/", 1)[-1]]
    return schema


def _minimal(schema: dict):
    """The smallest value the schema accepts: null where it may be null."""
    schema = _resolve(schema)
    if schema.get("nullable") or schema.get("type") == "null":
        return None
    for key in ("anyOf", "oneOf"):
        if key in schema:
            options = [_resolve(o) for o in schema[key]]
            if any(o.get("type") == "null" or o.get("nullable") for o in options):
                return None
            return _minimal(options[0])
    if "allOf" in schema:
        merged: dict = {}
        for part in schema["allOf"]:
            value = _minimal(part)
            if isinstance(value, dict):
                merged.update(value)
        return merged
    if "enum" in schema:
        return schema["enum"][0]
    kind = schema.get("type")
    if isinstance(kind, list):
        return None if "null" in kind else _minimal({**schema, "type": kind[0]})
    if kind == "object" or "properties" in schema:
        props = schema.get("properties", {})
        return {name: _minimal(props[name]) for name in schema.get("required", []) if name in props}
    if kind == "array":
        return []
    if kind == "boolean":
        return False
    if kind in ("integer", "number"):
        return 0
    if schema.get("format") == "date-time":
        return "2026-09-03T08:15:02.113Z"
    return "x"


def _merge(base, overrides):
    if isinstance(base, dict) and isinstance(overrides, dict):
        return {**base, **{k: _merge(base.get(k), v) for k, v in overrides.items()}}
    return overrides


def sample(name: str, **overrides):
    """A response of this schema with every required field, then the test's own values."""
    return _merge(_minimal(SCHEMAS[name]), overrides)


MENTION = sample(
    "Mention",
    id="mm_1",
    status="open",
    relevant=True,
    priority=61.5,
    keyword={"id": "kw_1", "term": "acme", "group": {"id": "grp_1", "name": "Default", "externalId": None, "isDefault": True}},
    post={"platform": "reddit", "url": "https://r/1", "text": "hi", "subreddit": "SaaS", "publishedAt": "2026-09-03T08:12:44.000Z"},
)
KEYWORD = sample("Keyword", id="kw_1", term="acme", kind="brand", createdAt="2026-09-03T10:04:44.881Z")


def test_the_samples_carry_every_required_field():
    # What the generated models insist on, read off the spec: a response
    # that gains a required field gets it here without anyone editing a test.
    for name, value in (("Mention", MENTION), ("Keyword", KEYWORD)):
        assert set(SCHEMAS[name]["required"]) <= set(value), name
    assert KEYWORD["matching"]["subreddits"] == {"only": [], "excluded": []}
    assert KEYWORD["feeds"] == []


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
        return json_response(201, KEYWORD)

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
        return json_response(201, {"id": "dest_1", "kind": "webhook", "label": "Production", "config": {"url": "https://example.com/hook", "headers": {}, "events": [], "secret": "whsec_x"}, "stats": {"alerts": 0, "activeAlerts": 0, "lastDeliveryAt": None, "last7d": {"total": 0, "failed": 0}}, "createdAt": "2026-09-03T10:04:44.881Z"})

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
