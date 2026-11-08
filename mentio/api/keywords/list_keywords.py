from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_keywords_kind_item import ListKeywordsKindItem
from ...models.list_keywords_kinds_item import ListKeywordsKindsItem
from ...models.list_keywords_not_kinds_item import ListKeywordsNotKindsItem
from ...models.list_keywords_not_platforms_item import ListKeywordsNotPlatformsItem
from ...models.list_keywords_not_statuses_item import ListKeywordsNotStatusesItem
from ...models.list_keywords_platform_item import ListKeywordsPlatformItem
from ...models.list_keywords_platforms_item import ListKeywordsPlatformsItem
from ...models.list_keywords_response_200 import ListKeywordsResponse200
from ...models.list_keywords_sort import ListKeywordsSort
from ...models.list_keywords_status_item import ListKeywordsStatusItem
from ...models.list_keywords_statuses_item import ListKeywordsStatusesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    kinds: list[ListKeywordsKindsItem] | Unset = UNSET,
    not_kinds: list[ListKeywordsNotKindsItem] | Unset = UNSET,
    not_statuses: list[ListKeywordsNotStatusesItem] | Unset = UNSET,
    not_platforms: list[ListKeywordsNotPlatformsItem] | Unset = UNSET,
    statuses: list[ListKeywordsStatusesItem] | Unset = UNSET,
    platforms: list[ListKeywordsPlatformsItem] | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    json_group_ids: list[str] | None | Unset
    if isinstance(group_ids, Unset):
        json_group_ids = UNSET
    elif isinstance(group_ids, list):
        json_group_ids = group_ids

    else:
        json_group_ids = group_ids
    params["groupIds"] = json_group_ids

    json_not_group_ids: list[str] | None | Unset
    if isinstance(not_group_ids, Unset):
        json_not_group_ids = UNSET
    elif isinstance(not_group_ids, list):
        json_not_group_ids = not_group_ids

    else:
        json_not_group_ids = not_group_ids
    params["notGroupIds"] = json_not_group_ids

    json_kinds: list[str] | Unset = UNSET
    if not isinstance(kinds, Unset):
        json_kinds = []
        for kinds_item_data in kinds:
            kinds_item = kinds_item_data.value
            json_kinds.append(kinds_item)

    params["kinds"] = json_kinds

    json_not_kinds: list[str] | Unset = UNSET
    if not isinstance(not_kinds, Unset):
        json_not_kinds = []
        for not_kinds_item_data in not_kinds:
            not_kinds_item = not_kinds_item_data.value
            json_not_kinds.append(not_kinds_item)

    params["notKinds"] = json_not_kinds

    json_not_statuses: list[str] | Unset = UNSET
    if not isinstance(not_statuses, Unset):
        json_not_statuses = []
        for not_statuses_item_data in not_statuses:
            not_statuses_item = not_statuses_item_data.value
            json_not_statuses.append(not_statuses_item)

    params["notStatuses"] = json_not_statuses

    json_not_platforms: list[str] | Unset = UNSET
    if not isinstance(not_platforms, Unset):
        json_not_platforms = []
        for not_platforms_item_data in not_platforms:
            not_platforms_item = not_platforms_item_data.value
            json_not_platforms.append(not_platforms_item)

    params["notPlatforms"] = json_not_platforms

    json_statuses: list[str] | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = []
        for statuses_item_data in statuses:
            statuses_item = statuses_item_data.value
            json_statuses.append(statuses_item)

    params["statuses"] = json_statuses

    json_platforms: list[str] | Unset = UNSET
    if not isinstance(platforms, Unset):
        json_platforms = []
        for platforms_item_data in platforms:
            platforms_item = platforms_item_data.value
            json_platforms.append(platforms_item)

    params["platforms"] = json_platforms

    json_group_id: list[str] | None | Unset
    if isinstance(group_id, Unset):
        json_group_id = UNSET
    elif isinstance(group_id, list):
        json_group_id = group_id

    else:
        json_group_id = group_id
    params["groupId"] = json_group_id

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item = kind_item_data.value
            json_kind.append(kind_item)

    params["kind"] = json_kind

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_platform: list[str] | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = []
        for platform_item_data in platform:
            platform_item = platform_item_data.value
            json_platform.append(platform_item)

    params["platform"] = json_platform

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["limit"] = limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/keywords",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListKeywordsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListKeywordsResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    kinds: list[ListKeywordsKindsItem] | Unset = UNSET,
    not_kinds: list[ListKeywordsNotKindsItem] | Unset = UNSET,
    not_statuses: list[ListKeywordsNotStatusesItem] | Unset = UNSET,
    not_platforms: list[ListKeywordsNotPlatformsItem] | Unset = UNSET,
    statuses: list[ListKeywordsStatusesItem] | Unset = UNSET,
    platforms: list[ListKeywordsPlatformsItem] | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    """List keywords

     List the workspace's keywords with their match stats and poll health, newest first.

    `q` searches term and context; the other parameters filter, sort and page; `total` counts matches
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_ids (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        not_group_ids (list[str] | None | Unset): Never keywords in these groups (grp_...).
            Repeatable, or comma-separated.
        kinds (list[ListKeywordsKindsItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        not_kinds (list[ListKeywordsNotKindsItem] | Unset): Never these kinds. Repeatable, or
            comma-separated.
        not_statuses (list[ListKeywordsNotStatusesItem] | Unset): Never keywords in these states.
            Repeatable, or comma-separated.
        not_platforms (list[ListKeywordsNotPlatformsItem] | Unset): Never keywords tracked on any
            of these platforms (by the same reading as platforms). Repeatable, or comma-separated.
        statuses (list[ListKeywordsStatusesItem] | Unset): Only keywords in these states: active,
            muted, paused, noisy, capped. Repeatable, or comma-separated.
        platforms (list[ListKeywordsPlatformsItem] | Unset): Only keywords tracked on any of these
            platforms: its term searched there (every platform when its platforms are null), or for
            appstore and googleplay, an app of that store among its reviewSources. Repeatable, or
            comma-separated.
        group_id (list[str] | None | Unset): Deprecated: use groupIds, the same filter; both are
            read as one list.
        kind (list[ListKeywordsKindItem] | Unset): Deprecated: use kinds, the same filter; both
            are read as one list.
        status (list[ListKeywordsStatusItem] | Unset): Deprecated: use statuses, the same filter;
            both are read as one list.
        platform (list[ListKeywordsPlatformItem] | Unset): Deprecated: use platforms, the same
            filter; both are read as one list.
        sort (ListKeywordsSort | Unset): newest: created most recently first. oldest: the reverse.
            term: A to Z. mentions: most matches first. relevant: most relevant matches first. recent:
            most matches in the last 7 days first. lastMention: newest matched post first, keywords
            with none last. Default: ListKeywordsSort.NEWEST.
        limit (int | Unset): Page size, 1 to 500. Omit for every keyword after `offset`.
        offset (int | None | Unset): Skip this many keywords. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListKeywordsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        group_ids=group_ids,
        not_group_ids=not_group_ids,
        kinds=kinds,
        not_kinds=not_kinds,
        not_statuses=not_statuses,
        not_platforms=not_platforms,
        statuses=statuses,
        platforms=platforms,
        group_id=group_id,
        kind=kind,
        status=status,
        platform=platform,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    kinds: list[ListKeywordsKindsItem] | Unset = UNSET,
    not_kinds: list[ListKeywordsNotKindsItem] | Unset = UNSET,
    not_statuses: list[ListKeywordsNotStatusesItem] | Unset = UNSET,
    not_platforms: list[ListKeywordsNotPlatformsItem] | Unset = UNSET,
    statuses: list[ListKeywordsStatusesItem] | Unset = UNSET,
    platforms: list[ListKeywordsPlatformsItem] | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListKeywordsResponse200 | None:
    """List keywords

     List the workspace's keywords with their match stats and poll health, newest first.

    `q` searches term and context; the other parameters filter, sort and page; `total` counts matches
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_ids (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        not_group_ids (list[str] | None | Unset): Never keywords in these groups (grp_...).
            Repeatable, or comma-separated.
        kinds (list[ListKeywordsKindsItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        not_kinds (list[ListKeywordsNotKindsItem] | Unset): Never these kinds. Repeatable, or
            comma-separated.
        not_statuses (list[ListKeywordsNotStatusesItem] | Unset): Never keywords in these states.
            Repeatable, or comma-separated.
        not_platforms (list[ListKeywordsNotPlatformsItem] | Unset): Never keywords tracked on any
            of these platforms (by the same reading as platforms). Repeatable, or comma-separated.
        statuses (list[ListKeywordsStatusesItem] | Unset): Only keywords in these states: active,
            muted, paused, noisy, capped. Repeatable, or comma-separated.
        platforms (list[ListKeywordsPlatformsItem] | Unset): Only keywords tracked on any of these
            platforms: its term searched there (every platform when its platforms are null), or for
            appstore and googleplay, an app of that store among its reviewSources. Repeatable, or
            comma-separated.
        group_id (list[str] | None | Unset): Deprecated: use groupIds, the same filter; both are
            read as one list.
        kind (list[ListKeywordsKindItem] | Unset): Deprecated: use kinds, the same filter; both
            are read as one list.
        status (list[ListKeywordsStatusItem] | Unset): Deprecated: use statuses, the same filter;
            both are read as one list.
        platform (list[ListKeywordsPlatformItem] | Unset): Deprecated: use platforms, the same
            filter; both are read as one list.
        sort (ListKeywordsSort | Unset): newest: created most recently first. oldest: the reverse.
            term: A to Z. mentions: most matches first. relevant: most relevant matches first. recent:
            most matches in the last 7 days first. lastMention: newest matched post first, keywords
            with none last. Default: ListKeywordsSort.NEWEST.
        limit (int | Unset): Page size, 1 to 500. Omit for every keyword after `offset`.
        offset (int | None | Unset): Skip this many keywords. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListKeywordsResponse200
    """

    return sync_detailed(
        client=client,
        q=q,
        group_ids=group_ids,
        not_group_ids=not_group_ids,
        kinds=kinds,
        not_kinds=not_kinds,
        not_statuses=not_statuses,
        not_platforms=not_platforms,
        statuses=statuses,
        platforms=platforms,
        group_id=group_id,
        kind=kind,
        status=status,
        platform=platform,
        sort=sort,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    kinds: list[ListKeywordsKindsItem] | Unset = UNSET,
    not_kinds: list[ListKeywordsNotKindsItem] | Unset = UNSET,
    not_statuses: list[ListKeywordsNotStatusesItem] | Unset = UNSET,
    not_platforms: list[ListKeywordsNotPlatformsItem] | Unset = UNSET,
    statuses: list[ListKeywordsStatusesItem] | Unset = UNSET,
    platforms: list[ListKeywordsPlatformsItem] | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    """List keywords

     List the workspace's keywords with their match stats and poll health, newest first.

    `q` searches term and context; the other parameters filter, sort and page; `total` counts matches
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_ids (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        not_group_ids (list[str] | None | Unset): Never keywords in these groups (grp_...).
            Repeatable, or comma-separated.
        kinds (list[ListKeywordsKindsItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        not_kinds (list[ListKeywordsNotKindsItem] | Unset): Never these kinds. Repeatable, or
            comma-separated.
        not_statuses (list[ListKeywordsNotStatusesItem] | Unset): Never keywords in these states.
            Repeatable, or comma-separated.
        not_platforms (list[ListKeywordsNotPlatformsItem] | Unset): Never keywords tracked on any
            of these platforms (by the same reading as platforms). Repeatable, or comma-separated.
        statuses (list[ListKeywordsStatusesItem] | Unset): Only keywords in these states: active,
            muted, paused, noisy, capped. Repeatable, or comma-separated.
        platforms (list[ListKeywordsPlatformsItem] | Unset): Only keywords tracked on any of these
            platforms: its term searched there (every platform when its platforms are null), or for
            appstore and googleplay, an app of that store among its reviewSources. Repeatable, or
            comma-separated.
        group_id (list[str] | None | Unset): Deprecated: use groupIds, the same filter; both are
            read as one list.
        kind (list[ListKeywordsKindItem] | Unset): Deprecated: use kinds, the same filter; both
            are read as one list.
        status (list[ListKeywordsStatusItem] | Unset): Deprecated: use statuses, the same filter;
            both are read as one list.
        platform (list[ListKeywordsPlatformItem] | Unset): Deprecated: use platforms, the same
            filter; both are read as one list.
        sort (ListKeywordsSort | Unset): newest: created most recently first. oldest: the reverse.
            term: A to Z. mentions: most matches first. relevant: most relevant matches first. recent:
            most matches in the last 7 days first. lastMention: newest matched post first, keywords
            with none last. Default: ListKeywordsSort.NEWEST.
        limit (int | Unset): Page size, 1 to 500. Omit for every keyword after `offset`.
        offset (int | None | Unset): Skip this many keywords. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListKeywordsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        group_ids=group_ids,
        not_group_ids=not_group_ids,
        kinds=kinds,
        not_kinds=not_kinds,
        not_statuses=not_statuses,
        not_platforms=not_platforms,
        statuses=statuses,
        platforms=platforms,
        group_id=group_id,
        kind=kind,
        status=status,
        platform=platform,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    kinds: list[ListKeywordsKindsItem] | Unset = UNSET,
    not_kinds: list[ListKeywordsNotKindsItem] | Unset = UNSET,
    not_statuses: list[ListKeywordsNotStatusesItem] | Unset = UNSET,
    not_platforms: list[ListKeywordsNotPlatformsItem] | Unset = UNSET,
    statuses: list[ListKeywordsStatusesItem] | Unset = UNSET,
    platforms: list[ListKeywordsPlatformsItem] | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListKeywordsResponse200 | None:
    """List keywords

     List the workspace's keywords with their match stats and poll health, newest first.

    `q` searches term and context; the other parameters filter, sort and page; `total` counts matches
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_ids (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        not_group_ids (list[str] | None | Unset): Never keywords in these groups (grp_...).
            Repeatable, or comma-separated.
        kinds (list[ListKeywordsKindsItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        not_kinds (list[ListKeywordsNotKindsItem] | Unset): Never these kinds. Repeatable, or
            comma-separated.
        not_statuses (list[ListKeywordsNotStatusesItem] | Unset): Never keywords in these states.
            Repeatable, or comma-separated.
        not_platforms (list[ListKeywordsNotPlatformsItem] | Unset): Never keywords tracked on any
            of these platforms (by the same reading as platforms). Repeatable, or comma-separated.
        statuses (list[ListKeywordsStatusesItem] | Unset): Only keywords in these states: active,
            muted, paused, noisy, capped. Repeatable, or comma-separated.
        platforms (list[ListKeywordsPlatformsItem] | Unset): Only keywords tracked on any of these
            platforms: its term searched there (every platform when its platforms are null), or for
            appstore and googleplay, an app of that store among its reviewSources. Repeatable, or
            comma-separated.
        group_id (list[str] | None | Unset): Deprecated: use groupIds, the same filter; both are
            read as one list.
        kind (list[ListKeywordsKindItem] | Unset): Deprecated: use kinds, the same filter; both
            are read as one list.
        status (list[ListKeywordsStatusItem] | Unset): Deprecated: use statuses, the same filter;
            both are read as one list.
        platform (list[ListKeywordsPlatformItem] | Unset): Deprecated: use platforms, the same
            filter; both are read as one list.
        sort (ListKeywordsSort | Unset): newest: created most recently first. oldest: the reverse.
            term: A to Z. mentions: most matches first. relevant: most relevant matches first. recent:
            most matches in the last 7 days first. lastMention: newest matched post first, keywords
            with none last. Default: ListKeywordsSort.NEWEST.
        limit (int | Unset): Page size, 1 to 500. Omit for every keyword after `offset`.
        offset (int | None | Unset): Skip this many keywords. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListKeywordsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            group_ids=group_ids,
            not_group_ids=not_group_ids,
            kinds=kinds,
            not_kinds=not_kinds,
            not_statuses=not_statuses,
            not_platforms=not_platforms,
            statuses=statuses,
            platforms=platforms,
            group_id=group_id,
            kind=kind,
            status=status,
            platform=platform,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed
