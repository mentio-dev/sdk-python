import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.search_mentions_platform import SearchMentionsPlatform
from ...models.search_mentions_response_200 import SearchMentionsResponse200
from ...models.search_mentions_sentiment import SearchMentionsSentiment
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
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
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

    json_min_followers: int | None | Unset
    if isinstance(min_followers, Unset):
        json_min_followers = UNSET
    else:
        json_min_followers = min_followers
    params["minFollowers"] = json_min_followers

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
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
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
    the same filters and sort. A mention is one post matched to one keyword.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent (buy_intent, question, complaint,
            praise, comparison).
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
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        q (str | Unset): Substring search in the post text.
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
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_followers=min_followers,
        tags=tags,
        link_hosts=link_hosts,
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
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
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
    the same filters and sort. A mention is one post matched to one keyword.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent (buy_intent, question, complaint,
            praise, comparison).
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
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        q (str | Unset): Substring search in the post text.
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
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_followers=min_followers,
        tags=tags,
        link_hosts=link_hosts,
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
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
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
    the same filters and sort. A mention is one post matched to one keyword.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent (buy_intent, question, complaint,
            praise, comparison).
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
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        q (str | Unset): Substring search in the post text.
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
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_followers=min_followers,
        tags=tags,
        link_hosts=link_hosts,
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
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
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
    the same filters and sort. A mention is one post matched to one keyword.

    Args:
        keyword_id (str | Unset): Only matches of this keyword.
        platform (SearchMentionsPlatform | Unset): Only posts from this platform.
        status (SearchMentionsStatus | Unset): Only mentions in this status. Omit for every
            status.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only
            the rest (unclassified included).
        sentiment (SearchMentionsSentiment | Unset): Only this sentiment.
        intent (str | Unset): Only mentions carrying this intent (buy_intent, question, complaint,
            praise, comparison).
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
        min_followers (int | None | Unset): Only authors with at least this many followers.
            Unknown reach never passes.
        tags (list[str] | None | Unset): Only authors your workspace tagged with any of these
            (exact, case-sensitive). Repeatable, or comma-separated.
        link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host
            itself or a subdomain of it (octolens.com also matches blog.octolens.com). Repeatable, or
            comma-separated.
        q (str | Unset): Substring search in the post text.
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
            person_id=person_id,
            include_muted=include_muted,
            assignee_id=assignee_id,
            snoozed=snoozed,
            exclude_authors=exclude_authors,
            min_relevance=min_relevance,
            min_followers=min_followers,
            tags=tags,
            link_hosts=link_hosts,
            q=q,
            since=since,
            until=until,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
