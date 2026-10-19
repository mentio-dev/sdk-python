from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_feeds_response_200 import ListFeedsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

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
        "url": "/v1/feeds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListFeedsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListFeedsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ListFeedsResponse200]:
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
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListFeedsResponse200]:
    """List feeds

     The RSS and Atom feeds the workspace reads (forums, communities, blogs), newest connection first,
    each with how its hourly poll goes. Every keyword of the workspace with readsWorkspaceFeeds (the
    default) reads these feeds: an item holding its term is one of its mentions, with its matching
    rules, billed like any mention. Each feed is read every hour; reading it is free. At most 500 a
    workspace.

    Args:
        q (str | Unset): Only feeds whose address or title contains this text, case-insensitive.
        limit (int | Unset): Feeds per page, at most 500; default 100. Default: 100.
        offset (int | None | Unset): Feeds to skip, for the next page. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListFeedsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
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
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListFeedsResponse200 | None:
    """List feeds

     The RSS and Atom feeds the workspace reads (forums, communities, blogs), newest connection first,
    each with how its hourly poll goes. Every keyword of the workspace with readsWorkspaceFeeds (the
    default) reads these feeds: an item holding its term is one of its mentions, with its matching
    rules, billed like any mention. Each feed is read every hour; reading it is free. At most 500 a
    workspace.

    Args:
        q (str | Unset): Only feeds whose address or title contains this text, case-insensitive.
        limit (int | Unset): Feeds per page, at most 500; default 100. Default: 100.
        offset (int | None | Unset): Feeds to skip, for the next page. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListFeedsResponse200
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListFeedsResponse200]:
    """List feeds

     The RSS and Atom feeds the workspace reads (forums, communities, blogs), newest connection first,
    each with how its hourly poll goes. Every keyword of the workspace with readsWorkspaceFeeds (the
    default) reads these feeds: an item holding its term is one of its mentions, with its matching
    rules, billed like any mention. Each feed is read every hour; reading it is free. At most 500 a
    workspace.

    Args:
        q (str | Unset): Only feeds whose address or title contains this text, case-insensitive.
        limit (int | Unset): Feeds per page, at most 500; default 100. Default: 100.
        offset (int | None | Unset): Feeds to skip, for the next page. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListFeedsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListFeedsResponse200 | None:
    """List feeds

     The RSS and Atom feeds the workspace reads (forums, communities, blogs), newest connection first,
    each with how its hourly poll goes. Every keyword of the workspace with readsWorkspaceFeeds (the
    default) reads these feeds: an item holding its term is one of its mentions, with its matching
    rules, billed like any mention. Each feed is read every hour; reading it is free. At most 500 a
    workspace.

    Args:
        q (str | Unset): Only feeds whose address or title contains this text, case-insensitive.
        limit (int | Unset): Feeds per page, at most 500; default 100. Default: 100.
        offset (int | None | Unset): Feeds to skip, for the next page. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListFeedsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
            offset=offset,
        )
    ).parsed
