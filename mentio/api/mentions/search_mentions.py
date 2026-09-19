import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.search_mentions_not_platforms_item import SearchMentionsNotPlatformsItem
from ...models.search_mentions_not_sentiments_item import (
    SearchMentionsNotSentimentsItem,
)
from ...models.search_mentions_platform import SearchMentionsPlatform
from ...models.search_mentions_platforms_item import SearchMentionsPlatformsItem
from ...models.search_mentions_response_200 import SearchMentionsResponse200
from ...models.search_mentions_sentiment import SearchMentionsSentiment
from ...models.search_mentions_sentiments_item import SearchMentionsSentimentsItem
from ...models.search_mentions_sort import SearchMentionsSort
from ...models.search_mentions_status import SearchMentionsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keyword_id: str | Unset = UNSET,
    platform: SearchMentionsPlatform | Unset = UNSET,
    status: SearchMentionsStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: SearchMentionsSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[SearchMentionsPlatformsItem] | Unset = UNSET,
    not_platforms: list[SearchMentionsNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[SearchMentionsSentimentsItem] | Unset = UNSET,
    not_sentiments: list[SearchMentionsNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    sort: SearchMentionsSort | Unset = SearchMentionsSort.NEWEST,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["keywordId"] = keyword_id

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["relevant"] = relevant

    json_sentiment: str | Unset = UNSET
    if not isinstance(sentiment, Unset):
        json_sentiment = sentiment.value

    params["sentiment"] = json_sentiment

    params["intent"] = intent

    params["automated"] = automated

    params["personId"] = person_id

    params["includeMuted"] = include_muted

    params["assigneeId"] = assignee_id

    params["snoozed"] = snoozed

    json_exclude_authors: list[str] | None | Unset
    if isinstance(exclude_authors, Unset):
        json_exclude_authors = UNSET
    elif isinstance(exclude_authors, list):
        json_exclude_authors = exclude_authors

    else:
        json_exclude_authors = exclude_authors
    params["excludeAuthors"] = json_exclude_authors

    json_min_relevance: int | None | Unset
    if isinstance(min_relevance, Unset):
        json_min_relevance = UNSET
    else:
        json_min_relevance = min_relevance
    params["minRelevance"] = json_min_relevance

    json_min_confidence: float | None | Unset
    if isinstance(min_confidence, Unset):
        json_min_confidence = UNSET
    else:
        json_min_confidence = min_confidence
    params["minConfidence"] = json_min_confidence

    json_min_followers: int | None | Unset
    if isinstance(min_followers, Unset):
        json_min_followers = UNSET
    else:
        json_min_followers = min_followers
    params["minFollowers"] = json_min_followers

    json_max_followers: int | None | Unset
    if isinstance(max_followers, Unset):
        json_max_followers = UNSET
    else:
        json_max_followers = max_followers
    params["maxFollowers"] = json_max_followers

    params["isReply"] = is_reply

    params["alertId"] = alert_id

    json_tags: list[str] | None | Unset
    if isinstance(tags, Unset):
        json_tags = UNSET
    elif isinstance(tags, list):
        json_tags = tags

    else:
        json_tags = tags
    params["tags"] = json_tags

    json_link_hosts: list[str] | None | Unset
    if isinstance(link_hosts, Unset):
        json_link_hosts = UNSET
    elif isinstance(link_hosts, list):
        json_link_hosts = link_hosts

    else:
        json_link_hosts = link_hosts
    params["linkHosts"] = json_link_hosts

    json_platforms: list[str] | Unset = UNSET
    if not isinstance(platforms, Unset):
        json_platforms = []
        for platforms_item_data in platforms:
            platforms_item = platforms_item_data.value
            json_platforms.append(platforms_item)

    params["platforms"] = json_platforms

    json_not_platforms: list[str] | Unset = UNSET
    if not isinstance(not_platforms, Unset):
        json_not_platforms = []
        for not_platforms_item_data in not_platforms:
            not_platforms_item = not_platforms_item_data.value
            json_not_platforms.append(not_platforms_item)

    params["notPlatforms"] = json_not_platforms

    json_keyword_ids: list[str] | None | Unset
    if isinstance(keyword_ids, Unset):
        json_keyword_ids = UNSET
    elif isinstance(keyword_ids, list):
        json_keyword_ids = keyword_ids

    else:
        json_keyword_ids = keyword_ids
    params["keywordIds"] = json_keyword_ids

    json_not_keyword_ids: list[str] | None | Unset
    if isinstance(not_keyword_ids, Unset):
        json_not_keyword_ids = UNSET
    elif isinstance(not_keyword_ids, list):
        json_not_keyword_ids = not_keyword_ids

    else:
        json_not_keyword_ids = not_keyword_ids
    params["notKeywordIds"] = json_not_keyword_ids

    json_sentiments: list[str] | Unset = UNSET
    if not isinstance(sentiments, Unset):
        json_sentiments = []
        for sentiments_item_data in sentiments:
            sentiments_item = sentiments_item_data.value
            json_sentiments.append(sentiments_item)

    params["sentiments"] = json_sentiments

    json_not_sentiments: list[str] | Unset = UNSET
    if not isinstance(not_sentiments, Unset):
        json_not_sentiments = []
        for not_sentiments_item_data in not_sentiments:
            not_sentiments_item = not_sentiments_item_data.value
            json_not_sentiments.append(not_sentiments_item)

    params["notSentiments"] = json_not_sentiments

    json_intents: list[str] | None | Unset
    if isinstance(intents, Unset):
        json_intents = UNSET
    elif isinstance(intents, list):
        json_intents = intents

    else:
        json_intents = intents
    params["intents"] = json_intents

    json_not_intents: list[str] | None | Unset
    if isinstance(not_intents, Unset):
        json_not_intents = UNSET
    elif isinstance(not_intents, list):
        json_not_intents = not_intents

    else:
        json_not_intents = not_intents
    params["notIntents"] = json_not_intents

    json_not_link_hosts: list[str] | None | Unset
    if isinstance(not_link_hosts, Unset):
        json_not_link_hosts = UNSET
    elif isinstance(not_link_hosts, list):
        json_not_link_hosts = not_link_hosts

    else:
        json_not_link_hosts = not_link_hosts
    params["notLinkHosts"] = json_not_link_hosts

    json_not_tags: list[str] | None | Unset
    if isinstance(not_tags, Unset):
        json_not_tags = UNSET
    elif isinstance(not_tags, list):
        json_not_tags = not_tags

    else:
        json_not_tags = not_tags
    params["notTags"] = json_not_tags

    json_languages: list[str] | Unset = UNSET
    if not isinstance(languages, Unset):
        json_languages = languages

    params["languages"] = json_languages

    json_not_languages: list[str] | Unset = UNSET
    if not isinstance(not_languages, Unset):
        json_not_languages = not_languages

    params["notLanguages"] = json_not_languages

    params["q"] = q

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/mentions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SearchMentionsResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchMentionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | SearchMentionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    keyword_id: str | Unset = UNSET,
    platform: SearchMentionsPlatform | Unset = UNSET,
    status: SearchMentionsStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: SearchMentionsSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[SearchMentionsPlatformsItem] | Unset = UNSET,
    not_platforms: list[SearchMentionsNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[SearchMentionsSentimentsItem] | Unset = UNSET,
    not_sentiments: list[SearchMentionsNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    sort: SearchMentionsSort | Unset = SearchMentionsSort.NEWEST,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[ErrorResponse | SearchMentionsResponse200]:
    """List mentions

     Mentions matched to your keywords, filtered and paginated. Default order is newest match first;
    sort=priority ranks the last 30 days of matches by attention score. Page with nextCursor, passing
    the same filters and sort. A mention is one post matched to one keyword. alertId applies an alert
    rule's filter on top of the others: the same mentions that rule would send.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent or topic tag (buy_intent,
            question, complaint, praise, comparison, churn_intent, bug_report, pricing, hiring, event,
            promotional).
        automated (bool | Unset): true: only mentions that read as machine-made (a bot account, a
            scheduled or templated post, AI-written text); false: only the rest, mentions judged
            before this existed included. Omitted: everything.
        person_id (str | Unset): Only this person (an id from /v1/people), merged accounts
            included. Implies includeMuted.
        include_muted (bool | Unset): true: include mentions by people you muted, hidden by
            default.
        assignee_id (str | Unset): Only mentions assigned to this workspace member (user id).
        snoozed (bool | Unset): true: only mentions currently snoozed. Otherwise snoozed mentions
            stay out until they wake.
        exclude_authors (list[str] | None | Unset): Hide these authors: display names, handles or
            profile URLs. Repeatable, or one comma-separated value.
        min_relevance (int | None | Unset): Only mentions scored at least this; unclassified ones
            are excluded.
        min_confidence (float | None | Unset): Only mentions whose classifier confidence is at
            least this, 0 to 1. Mentions without a confidence are excluded.
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        max_followers (int | None | Unset): Only authors with at most this many followers. Unknown
            reach never passes.
        is_reply (bool | Unset): true: only replies and comments (posts answering another post);
            false: only top-level posts. Omitted: both.
        alert_id (str | Unset): Apply an alert rule's filter (an id from GET /v1/alerts) on top of
            the other filters: the same mentions the rule would send, for a feed-shaped export or a
            preview. Unknown ids are a 404.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        platforms (list[SearchMentionsPlatformsItem] | Unset): Only posts from any of these
            platforms.
        not_platforms (list[SearchMentionsNotPlatformsItem] | Unset): Never posts from these
            platforms.
        keyword_ids (list[str] | None | Unset): Only matches of any of these keywords.
        not_keyword_ids (list[str] | None | Unset): Never matches of these keywords.
        sentiments (list[SearchMentionsSentimentsItem] | Unset): Only these sentiments.
        not_sentiments (list[SearchMentionsNotSentimentsItem] | Unset): Never these sentiments. A
            mention the classifier has not scored yet still passes.
        intents (list[str] | None | Unset): Only mentions carrying any of these intent or topic
            tags.
        not_intents (list[str] | None | Unset): Never mentions carrying these intent or topic
            tags.
        not_link_hosts (list[str] | None | Unset): Never posts linking to these hosts, the host
            itself or a subdomain of it.
        not_tags (list[str] | None | Unset): Never authors your workspace tagged with any of
            these.
        languages (list[str] | Unset): Only posts in any of these languages (ISO 639-1: en, es,
            de). A post whose language is unknown never passes.
        not_languages (list[str] | Unset): Never posts in these languages. A post whose language
            is unknown still passes.
        q (str | Unset): Substring search in the post text or the author's name.
        since (datetime.datetime | Unset): Only posts published at or after this instant (ISO
            8601, or epoch ms).
        until (datetime.datetime | Unset): Only posts published at or before this instant (ISO
            8601, or epoch ms).
        sort (SearchMentionsSort | Unset): newest: by match time, newest first. priority: by
            attention score, highest first; priority ranks the last 30 days of matches only, older
            ones stay reachable under newest. Cursors are specific to a sort. Default:
            SearchMentionsSort.NEWEST.
        cursor (str | Unset): nextCursor from the previous page; pass the same filters and sort.
        limit (int | Unset): Page size, 1 to 100. Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SearchMentionsResponse200]
    """

    kwargs = _get_kwargs(
        keyword_id=keyword_id,
        platform=platform,
        status=status,
        relevant=relevant,
        sentiment=sentiment,
        intent=intent,
        automated=automated,
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_confidence=min_confidence,
        min_followers=min_followers,
        max_followers=max_followers,
        is_reply=is_reply,
        alert_id=alert_id,
        tags=tags,
        link_hosts=link_hosts,
        platforms=platforms,
        not_platforms=not_platforms,
        keyword_ids=keyword_ids,
        not_keyword_ids=not_keyword_ids,
        sentiments=sentiments,
        not_sentiments=not_sentiments,
        intents=intents,
        not_intents=not_intents,
        not_link_hosts=not_link_hosts,
        not_tags=not_tags,
        languages=languages,
        not_languages=not_languages,
        q=q,
        since=since,
        until=until,
        sort=sort,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword_id: str | Unset = UNSET,
    platform: SearchMentionsPlatform | Unset = UNSET,
    status: SearchMentionsStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: SearchMentionsSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[SearchMentionsPlatformsItem] | Unset = UNSET,
    not_platforms: list[SearchMentionsNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[SearchMentionsSentimentsItem] | Unset = UNSET,
    not_sentiments: list[SearchMentionsNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    sort: SearchMentionsSort | Unset = SearchMentionsSort.NEWEST,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> ErrorResponse | SearchMentionsResponse200 | None:
    """List mentions

     Mentions matched to your keywords, filtered and paginated. Default order is newest match first;
    sort=priority ranks the last 30 days of matches by attention score. Page with nextCursor, passing
    the same filters and sort. A mention is one post matched to one keyword. alertId applies an alert
    rule's filter on top of the others: the same mentions that rule would send.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent or topic tag (buy_intent,
            question, complaint, praise, comparison, churn_intent, bug_report, pricing, hiring, event,
            promotional).
        automated (bool | Unset): true: only mentions that read as machine-made (a bot account, a
            scheduled or templated post, AI-written text); false: only the rest, mentions judged
            before this existed included. Omitted: everything.
        person_id (str | Unset): Only this person (an id from /v1/people), merged accounts
            included. Implies includeMuted.
        include_muted (bool | Unset): true: include mentions by people you muted, hidden by
            default.
        assignee_id (str | Unset): Only mentions assigned to this workspace member (user id).
        snoozed (bool | Unset): true: only mentions currently snoozed. Otherwise snoozed mentions
            stay out until they wake.
        exclude_authors (list[str] | None | Unset): Hide these authors: display names, handles or
            profile URLs. Repeatable, or one comma-separated value.
        min_relevance (int | None | Unset): Only mentions scored at least this; unclassified ones
            are excluded.
        min_confidence (float | None | Unset): Only mentions whose classifier confidence is at
            least this, 0 to 1. Mentions without a confidence are excluded.
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        max_followers (int | None | Unset): Only authors with at most this many followers. Unknown
            reach never passes.
        is_reply (bool | Unset): true: only replies and comments (posts answering another post);
            false: only top-level posts. Omitted: both.
        alert_id (str | Unset): Apply an alert rule's filter (an id from GET /v1/alerts) on top of
            the other filters: the same mentions the rule would send, for a feed-shaped export or a
            preview. Unknown ids are a 404.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        platforms (list[SearchMentionsPlatformsItem] | Unset): Only posts from any of these
            platforms.
        not_platforms (list[SearchMentionsNotPlatformsItem] | Unset): Never posts from these
            platforms.
        keyword_ids (list[str] | None | Unset): Only matches of any of these keywords.
        not_keyword_ids (list[str] | None | Unset): Never matches of these keywords.
        sentiments (list[SearchMentionsSentimentsItem] | Unset): Only these sentiments.
        not_sentiments (list[SearchMentionsNotSentimentsItem] | Unset): Never these sentiments. A
            mention the classifier has not scored yet still passes.
        intents (list[str] | None | Unset): Only mentions carrying any of these intent or topic
            tags.
        not_intents (list[str] | None | Unset): Never mentions carrying these intent or topic
            tags.
        not_link_hosts (list[str] | None | Unset): Never posts linking to these hosts, the host
            itself or a subdomain of it.
        not_tags (list[str] | None | Unset): Never authors your workspace tagged with any of
            these.
        languages (list[str] | Unset): Only posts in any of these languages (ISO 639-1: en, es,
            de). A post whose language is unknown never passes.
        not_languages (list[str] | Unset): Never posts in these languages. A post whose language
            is unknown still passes.
        q (str | Unset): Substring search in the post text or the author's name.
        since (datetime.datetime | Unset): Only posts published at or after this instant (ISO
            8601, or epoch ms).
        until (datetime.datetime | Unset): Only posts published at or before this instant (ISO
            8601, or epoch ms).
        sort (SearchMentionsSort | Unset): newest: by match time, newest first. priority: by
            attention score, highest first; priority ranks the last 30 days of matches only, older
            ones stay reachable under newest. Cursors are specific to a sort. Default:
            SearchMentionsSort.NEWEST.
        cursor (str | Unset): nextCursor from the previous page; pass the same filters and sort.
        limit (int | Unset): Page size, 1 to 100. Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SearchMentionsResponse200
    """

    return sync_detailed(
        client=client,
        keyword_id=keyword_id,
        platform=platform,
        status=status,
        relevant=relevant,
        sentiment=sentiment,
        intent=intent,
        automated=automated,
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_confidence=min_confidence,
        min_followers=min_followers,
        max_followers=max_followers,
        is_reply=is_reply,
        alert_id=alert_id,
        tags=tags,
        link_hosts=link_hosts,
        platforms=platforms,
        not_platforms=not_platforms,
        keyword_ids=keyword_ids,
        not_keyword_ids=not_keyword_ids,
        sentiments=sentiments,
        not_sentiments=not_sentiments,
        intents=intents,
        not_intents=not_intents,
        not_link_hosts=not_link_hosts,
        not_tags=not_tags,
        languages=languages,
        not_languages=not_languages,
        q=q,
        since=since,
        until=until,
        sort=sort,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword_id: str | Unset = UNSET,
    platform: SearchMentionsPlatform | Unset = UNSET,
    status: SearchMentionsStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: SearchMentionsSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[SearchMentionsPlatformsItem] | Unset = UNSET,
    not_platforms: list[SearchMentionsNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[SearchMentionsSentimentsItem] | Unset = UNSET,
    not_sentiments: list[SearchMentionsNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    sort: SearchMentionsSort | Unset = SearchMentionsSort.NEWEST,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[ErrorResponse | SearchMentionsResponse200]:
    """List mentions

     Mentions matched to your keywords, filtered and paginated. Default order is newest match first;
    sort=priority ranks the last 30 days of matches by attention score. Page with nextCursor, passing
    the same filters and sort. A mention is one post matched to one keyword. alertId applies an alert
    rule's filter on top of the others: the same mentions that rule would send.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent or topic tag (buy_intent,
            question, complaint, praise, comparison, churn_intent, bug_report, pricing, hiring, event,
            promotional).
        automated (bool | Unset): true: only mentions that read as machine-made (a bot account, a
            scheduled or templated post, AI-written text); false: only the rest, mentions judged
            before this existed included. Omitted: everything.
        person_id (str | Unset): Only this person (an id from /v1/people), merged accounts
            included. Implies includeMuted.
        include_muted (bool | Unset): true: include mentions by people you muted, hidden by
            default.
        assignee_id (str | Unset): Only mentions assigned to this workspace member (user id).
        snoozed (bool | Unset): true: only mentions currently snoozed. Otherwise snoozed mentions
            stay out until they wake.
        exclude_authors (list[str] | None | Unset): Hide these authors: display names, handles or
            profile URLs. Repeatable, or one comma-separated value.
        min_relevance (int | None | Unset): Only mentions scored at least this; unclassified ones
            are excluded.
        min_confidence (float | None | Unset): Only mentions whose classifier confidence is at
            least this, 0 to 1. Mentions without a confidence are excluded.
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        max_followers (int | None | Unset): Only authors with at most this many followers. Unknown
            reach never passes.
        is_reply (bool | Unset): true: only replies and comments (posts answering another post);
            false: only top-level posts. Omitted: both.
        alert_id (str | Unset): Apply an alert rule's filter (an id from GET /v1/alerts) on top of
            the other filters: the same mentions the rule would send, for a feed-shaped export or a
            preview. Unknown ids are a 404.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        platforms (list[SearchMentionsPlatformsItem] | Unset): Only posts from any of these
            platforms.
        not_platforms (list[SearchMentionsNotPlatformsItem] | Unset): Never posts from these
            platforms.
        keyword_ids (list[str] | None | Unset): Only matches of any of these keywords.
        not_keyword_ids (list[str] | None | Unset): Never matches of these keywords.
        sentiments (list[SearchMentionsSentimentsItem] | Unset): Only these sentiments.
        not_sentiments (list[SearchMentionsNotSentimentsItem] | Unset): Never these sentiments. A
            mention the classifier has not scored yet still passes.
        intents (list[str] | None | Unset): Only mentions carrying any of these intent or topic
            tags.
        not_intents (list[str] | None | Unset): Never mentions carrying these intent or topic
            tags.
        not_link_hosts (list[str] | None | Unset): Never posts linking to these hosts, the host
            itself or a subdomain of it.
        not_tags (list[str] | None | Unset): Never authors your workspace tagged with any of
            these.
        languages (list[str] | Unset): Only posts in any of these languages (ISO 639-1: en, es,
            de). A post whose language is unknown never passes.
        not_languages (list[str] | Unset): Never posts in these languages. A post whose language
            is unknown still passes.
        q (str | Unset): Substring search in the post text or the author's name.
        since (datetime.datetime | Unset): Only posts published at or after this instant (ISO
            8601, or epoch ms).
        until (datetime.datetime | Unset): Only posts published at or before this instant (ISO
            8601, or epoch ms).
        sort (SearchMentionsSort | Unset): newest: by match time, newest first. priority: by
            attention score, highest first; priority ranks the last 30 days of matches only, older
            ones stay reachable under newest. Cursors are specific to a sort. Default:
            SearchMentionsSort.NEWEST.
        cursor (str | Unset): nextCursor from the previous page; pass the same filters and sort.
        limit (int | Unset): Page size, 1 to 100. Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SearchMentionsResponse200]
    """

    kwargs = _get_kwargs(
        keyword_id=keyword_id,
        platform=platform,
        status=status,
        relevant=relevant,
        sentiment=sentiment,
        intent=intent,
        automated=automated,
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_confidence=min_confidence,
        min_followers=min_followers,
        max_followers=max_followers,
        is_reply=is_reply,
        alert_id=alert_id,
        tags=tags,
        link_hosts=link_hosts,
        platforms=platforms,
        not_platforms=not_platforms,
        keyword_ids=keyword_ids,
        not_keyword_ids=not_keyword_ids,
        sentiments=sentiments,
        not_sentiments=not_sentiments,
        intents=intents,
        not_intents=not_intents,
        not_link_hosts=not_link_hosts,
        not_tags=not_tags,
        languages=languages,
        not_languages=not_languages,
        q=q,
        since=since,
        until=until,
        sort=sort,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword_id: str | Unset = UNSET,
    platform: SearchMentionsPlatform | Unset = UNSET,
    status: SearchMentionsStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: SearchMentionsSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[SearchMentionsPlatformsItem] | Unset = UNSET,
    not_platforms: list[SearchMentionsNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[SearchMentionsSentimentsItem] | Unset = UNSET,
    not_sentiments: list[SearchMentionsNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    sort: SearchMentionsSort | Unset = SearchMentionsSort.NEWEST,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> ErrorResponse | SearchMentionsResponse200 | None:
    """List mentions

     Mentions matched to your keywords, filtered and paginated. Default order is newest match first;
    sort=priority ranks the last 30 days of matches by attention score. Page with nextCursor, passing
    the same filters and sort. A mention is one post matched to one keyword. alertId applies an alert
    rule's filter on top of the others: the same mentions that rule would send.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent or topic tag (buy_intent,
            question, complaint, praise, comparison, churn_intent, bug_report, pricing, hiring, event,
            promotional).
        automated (bool | Unset): true: only mentions that read as machine-made (a bot account, a
            scheduled or templated post, AI-written text); false: only the rest, mentions judged
            before this existed included. Omitted: everything.
        person_id (str | Unset): Only this person (an id from /v1/people), merged accounts
            included. Implies includeMuted.
        include_muted (bool | Unset): true: include mentions by people you muted, hidden by
            default.
        assignee_id (str | Unset): Only mentions assigned to this workspace member (user id).
        snoozed (bool | Unset): true: only mentions currently snoozed. Otherwise snoozed mentions
            stay out until they wake.
        exclude_authors (list[str] | None | Unset): Hide these authors: display names, handles or
            profile URLs. Repeatable, or one comma-separated value.
        min_relevance (int | None | Unset): Only mentions scored at least this; unclassified ones
            are excluded.
        min_confidence (float | None | Unset): Only mentions whose classifier confidence is at
            least this, 0 to 1. Mentions without a confidence are excluded.
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        max_followers (int | None | Unset): Only authors with at most this many followers. Unknown
            reach never passes.
        is_reply (bool | Unset): true: only replies and comments (posts answering another post);
            false: only top-level posts. Omitted: both.
        alert_id (str | Unset): Apply an alert rule's filter (an id from GET /v1/alerts) on top of
            the other filters: the same mentions the rule would send, for a feed-shaped export or a
            preview. Unknown ids are a 404.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        platforms (list[SearchMentionsPlatformsItem] | Unset): Only posts from any of these
            platforms.
        not_platforms (list[SearchMentionsNotPlatformsItem] | Unset): Never posts from these
            platforms.
        keyword_ids (list[str] | None | Unset): Only matches of any of these keywords.
        not_keyword_ids (list[str] | None | Unset): Never matches of these keywords.
        sentiments (list[SearchMentionsSentimentsItem] | Unset): Only these sentiments.
        not_sentiments (list[SearchMentionsNotSentimentsItem] | Unset): Never these sentiments. A
            mention the classifier has not scored yet still passes.
        intents (list[str] | None | Unset): Only mentions carrying any of these intent or topic
            tags.
        not_intents (list[str] | None | Unset): Never mentions carrying these intent or topic
            tags.
        not_link_hosts (list[str] | None | Unset): Never posts linking to these hosts, the host
            itself or a subdomain of it.
        not_tags (list[str] | None | Unset): Never authors your workspace tagged with any of
            these.
        languages (list[str] | Unset): Only posts in any of these languages (ISO 639-1: en, es,
            de). A post whose language is unknown never passes.
        not_languages (list[str] | Unset): Never posts in these languages. A post whose language
            is unknown still passes.
        q (str | Unset): Substring search in the post text or the author's name.
        since (datetime.datetime | Unset): Only posts published at or after this instant (ISO
            8601, or epoch ms).
        until (datetime.datetime | Unset): Only posts published at or before this instant (ISO
            8601, or epoch ms).
        sort (SearchMentionsSort | Unset): newest: by match time, newest first. priority: by
            attention score, highest first; priority ranks the last 30 days of matches only, older
            ones stay reachable under newest. Cursors are specific to a sort. Default:
            SearchMentionsSort.NEWEST.
        cursor (str | Unset): nextCursor from the previous page; pass the same filters and sort.
        limit (int | Unset): Page size, 1 to 100. Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SearchMentionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword_id=keyword_id,
            platform=platform,
            status=status,
            relevant=relevant,
            sentiment=sentiment,
            intent=intent,
            automated=automated,
            person_id=person_id,
            include_muted=include_muted,
            assignee_id=assignee_id,
            snoozed=snoozed,
            exclude_authors=exclude_authors,
            min_relevance=min_relevance,
            min_confidence=min_confidence,
            min_followers=min_followers,
            max_followers=max_followers,
            is_reply=is_reply,
            alert_id=alert_id,
            tags=tags,
            link_hosts=link_hosts,
            platforms=platforms,
            not_platforms=not_platforms,
            keyword_ids=keyword_ids,
            not_keyword_ids=not_keyword_ids,
            sentiments=sentiments,
            not_sentiments=not_sentiments,
            intents=intents,
            not_intents=not_intents,
            not_link_hosts=not_link_hosts,
            not_tags=not_tags,
            languages=languages,
            not_languages=not_languages,
            q=q,
            since=since,
            until=until,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
