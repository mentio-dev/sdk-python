from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_keywords_kind_item import ListKeywordsKindItem
from ...models.list_keywords_platform_item import ListKeywordsPlatformItem
from ...models.list_keywords_response_200 import ListKeywordsResponse200
from ...models.list_keywords_sort import ListKeywordsSort
from ...models.list_keywords_status_item import ListKeywordsStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
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
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    """List keywords

     The keywords of the workspace with their match stats and poll health. Without parameters: every
    keyword, newest first. `q` searches the term and the context; `kind`, `status` and `platform` narrow
    the list; `sort` orders it; `limit` and `offset` page it. `total` counts the keywords that matched
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_id (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        kind (list[ListKeywordsKindItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        status (list[ListKeywordsStatusItem] | Unset): Only keywords in these states: active,
            muted, paused, capped. Repeatable, or comma-separated.
        platform (list[ListKeywordsPlatformItem] | Unset): Only keywords tracked on any of these
            platforms; a keyword tracked everywhere always passes. Repeatable, or comma-separated.
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
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListKeywordsResponse200 | None:
    """List keywords

     The keywords of the workspace with their match stats and poll health. Without parameters: every
    keyword, newest first. `q` searches the term and the context; `kind`, `status` and `platform` narrow
    the list; `sort` orders it; `limit` and `offset` page it. `total` counts the keywords that matched
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_id (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        kind (list[ListKeywordsKindItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        status (list[ListKeywordsStatusItem] | Unset): Only keywords in these states: active,
            muted, paused, capped. Repeatable, or comma-separated.
        platform (list[ListKeywordsPlatformItem] | Unset): Only keywords tracked on any of these
            platforms; a keyword tracked everywhere always passes. Repeatable, or comma-separated.
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
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    """List keywords

     The keywords of the workspace with their match stats and poll health. Without parameters: every
    keyword, newest first. `q` searches the term and the context; `kind`, `status` and `platform` narrow
    the list; `sort` orders it; `limit` and `offset` page it. `total` counts the keywords that matched
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_id (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        kind (list[ListKeywordsKindItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        status (list[ListKeywordsStatusItem] | Unset): Only keywords in these states: active,
            muted, paused, capped. Repeatable, or comma-separated.
        platform (list[ListKeywordsPlatformItem] | Unset): Only keywords tracked on any of these
            platforms; a keyword tracked everywhere always passes. Repeatable, or comma-separated.
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
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListKeywordsResponse200 | None:
    """List keywords

     The keywords of the workspace with their match stats and poll health. Without parameters: every
    keyword, newest first. `q` searches the term and the context; `kind`, `status` and `platform` narrow
    the list; `sort` orders it; `limit` and `offset` page it. `total` counts the keywords that matched
    before paging.

    Args:
        q (str | Unset): Text to find in the term or in the keyword's context, case-insensitive.
        group_id (list[str] | None | Unset): Only keywords in any of these groups (grp_...).
            Repeatable, or comma-separated.
        kind (list[ListKeywordsKindItem] | Unset): Only these kinds: brand, competitor, topic.
            Repeatable, or comma-separated.
        status (list[ListKeywordsStatusItem] | Unset): Only keywords in these states: active,
            muted, paused, capped. Repeatable, or comma-separated.
        platform (list[ListKeywordsPlatformItem] | Unset): Only keywords tracked on any of these
            platforms; a keyword tracked everywhere always passes. Repeatable, or comma-separated.
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
            group_id=group_id,
            kind=kind,
            status=status,
            platform=platform,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed
