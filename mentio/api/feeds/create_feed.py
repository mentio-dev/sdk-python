from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_feed_body import CreateFeedBody
from ...models.error_response import ErrorResponse
from ...models.feed import Feed
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFeedBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/feeds",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Feed | None:
    if response.status_code == 200:
        response_200 = Feed.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Feed.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Feed]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFeedBody,
) -> Response[ErrorResponse | Feed]:
    """Connect a feed

     Connect an RSS or Atom feed: a feed's address, or a page's (a forum, a community, a blog), in which
    case the feed the page advertises is used, else a usual address such as /feed or /rss. Every keyword
    of the workspace with readsWorkspaceFeeds (the default) reads these feeds: an item holding its term
    is one of its mentions, with its matching rules, billed like any mention. Each feed is read every
    hour; reading it is free. At most 500 a workspace. A new feed brings each reading keyword the newest
    10 items of the last 30 days that hold its term, never as instant alerts. A feed the workspace reads
    already comes back with 200 (connecting is idempotent). A members-only forum answers
    `feed_login_required`: send it again with `auth` (a cookie or a header), stored encrypted and read
    for this workspace alone.

    Args:
        body (CreateFeedBody): One feed to connect, with a sign-in when it is members-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Feed]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateFeedBody,
) -> ErrorResponse | Feed | None:
    """Connect a feed

     Connect an RSS or Atom feed: a feed's address, or a page's (a forum, a community, a blog), in which
    case the feed the page advertises is used, else a usual address such as /feed or /rss. Every keyword
    of the workspace with readsWorkspaceFeeds (the default) reads these feeds: an item holding its term
    is one of its mentions, with its matching rules, billed like any mention. Each feed is read every
    hour; reading it is free. At most 500 a workspace. A new feed brings each reading keyword the newest
    10 items of the last 30 days that hold its term, never as instant alerts. A feed the workspace reads
    already comes back with 200 (connecting is idempotent). A members-only forum answers
    `feed_login_required`: send it again with `auth` (a cookie or a header), stored encrypted and read
    for this workspace alone.

    Args:
        body (CreateFeedBody): One feed to connect, with a sign-in when it is members-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Feed
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFeedBody,
) -> Response[ErrorResponse | Feed]:
    """Connect a feed

     Connect an RSS or Atom feed: a feed's address, or a page's (a forum, a community, a blog), in which
    case the feed the page advertises is used, else a usual address such as /feed or /rss. Every keyword
    of the workspace with readsWorkspaceFeeds (the default) reads these feeds: an item holding its term
    is one of its mentions, with its matching rules, billed like any mention. Each feed is read every
    hour; reading it is free. At most 500 a workspace. A new feed brings each reading keyword the newest
    10 items of the last 30 days that hold its term, never as instant alerts. A feed the workspace reads
    already comes back with 200 (connecting is idempotent). A members-only forum answers
    `feed_login_required`: send it again with `auth` (a cookie or a header), stored encrypted and read
    for this workspace alone.

    Args:
        body (CreateFeedBody): One feed to connect, with a sign-in when it is members-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Feed]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateFeedBody,
) -> ErrorResponse | Feed | None:
    """Connect a feed

     Connect an RSS or Atom feed: a feed's address, or a page's (a forum, a community, a blog), in which
    case the feed the page advertises is used, else a usual address such as /feed or /rss. Every keyword
    of the workspace with readsWorkspaceFeeds (the default) reads these feeds: an item holding its term
    is one of its mentions, with its matching rules, billed like any mention. Each feed is read every
    hour; reading it is free. At most 500 a workspace. A new feed brings each reading keyword the newest
    10 items of the last 30 days that hold its term, never as instant alerts. A feed the workspace reads
    already comes back with 200 (connecting is idempotent). A members-only forum answers
    `feed_login_required`: send it again with `auth` (a cookie or a header), stored encrypted and read
    for this workspace alone.

    Args:
        body (CreateFeedBody): One feed to connect, with a sign-in when it is members-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Feed
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
