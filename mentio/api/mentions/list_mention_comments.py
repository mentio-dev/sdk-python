from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_mention_comments_response_200 import ListMentionCommentsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/mentions/{id}/comments".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListMentionCommentsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListMentionCommentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ListMentionCommentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ErrorResponse | ListMentionCommentsResponse200]:
    """List the comments of a mention

     The comments under a mention's post, newest first: every comment in the thread, whether or not it
    names your keyword. Read once, about a day after the post, for mentions scored relevant whose
    keyword has comments enabled (keywords.comments), on Hacker News, Bluesky, GitHub, Stack Overflow,
    DEV, YouTube and Reddit; empty before that and for other keywords. Each comment delivered costs
    $0.008 on the comments line of the bill, once per workspace. A comment that itself names one of your
    keywords is also a mention: `mentionId` links it. Two mentions of one post (two keywords) list the
    same thread.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        cursor (str | Unset): nextCursor from the previous page.
        limit (int | Unset): Page size, 1 to 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListMentionCommentsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> ErrorResponse | ListMentionCommentsResponse200 | None:
    """List the comments of a mention

     The comments under a mention's post, newest first: every comment in the thread, whether or not it
    names your keyword. Read once, about a day after the post, for mentions scored relevant whose
    keyword has comments enabled (keywords.comments), on Hacker News, Bluesky, GitHub, Stack Overflow,
    DEV, YouTube and Reddit; empty before that and for other keywords. Each comment delivered costs
    $0.008 on the comments line of the bill, once per workspace. A comment that itself names one of your
    keywords is also a mention: `mentionId` links it. Two mentions of one post (two keywords) list the
    same thread.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        cursor (str | Unset): nextCursor from the previous page.
        limit (int | Unset): Page size, 1 to 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListMentionCommentsResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ErrorResponse | ListMentionCommentsResponse200]:
    """List the comments of a mention

     The comments under a mention's post, newest first: every comment in the thread, whether or not it
    names your keyword. Read once, about a day after the post, for mentions scored relevant whose
    keyword has comments enabled (keywords.comments), on Hacker News, Bluesky, GitHub, Stack Overflow,
    DEV, YouTube and Reddit; empty before that and for other keywords. Each comment delivered costs
    $0.008 on the comments line of the bill, once per workspace. A comment that itself names one of your
    keywords is also a mention: `mentionId` links it. Two mentions of one post (two keywords) list the
    same thread.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        cursor (str | Unset): nextCursor from the previous page.
        limit (int | Unset): Page size, 1 to 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListMentionCommentsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> ErrorResponse | ListMentionCommentsResponse200 | None:
    """List the comments of a mention

     The comments under a mention's post, newest first: every comment in the thread, whether or not it
    names your keyword. Read once, about a day after the post, for mentions scored relevant whose
    keyword has comments enabled (keywords.comments), on Hacker News, Bluesky, GitHub, Stack Overflow,
    DEV, YouTube and Reddit; empty before that and for other keywords. Each comment delivered costs
    $0.008 on the comments line of the bill, once per workspace. A comment that itself names one of your
    keywords is also a mention: `mentionId` links it. Two mentions of one post (two keywords) list the
    same thread.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        cursor (str | Unset): nextCursor from the previous page.
        limit (int | Unset): Page size, 1 to 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListMentionCommentsResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
