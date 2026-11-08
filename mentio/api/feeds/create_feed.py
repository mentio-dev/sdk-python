from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_feed_body import CreateFeedBody
from ...models.error_response import ErrorResponse
from ...models.feed import Feed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateFeedBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

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
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | Feed]:
    """Connect a feed

     Connect an RSS or Atom feed, or a page advertising one, for the workspace's keywords to read hourly.

    - Idempotent: a feed already read returns 200.
    - A members-only forum answers `feed_login_required`: resend with `auth`.

    See [RSS](/platforms/rss#workspace-feeds).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateFeedBody): One feed to connect, with a sign-in when it is members-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Feed]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateFeedBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | Feed | None:
    """Connect a feed

     Connect an RSS or Atom feed, or a page advertising one, for the workspace's keywords to read hourly.

    - Idempotent: a feed already read returns 200.
    - A members-only forum answers `feed_login_required`: resend with `auth`.

    See [RSS](/platforms/rss#workspace-feeds).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
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
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFeedBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | Feed]:
    """Connect a feed

     Connect an RSS or Atom feed, or a page advertising one, for the workspace's keywords to read hourly.

    - Idempotent: a feed already read returns 200.
    - A members-only forum answers `feed_login_required`: resend with `auth`.

    See [RSS](/platforms/rss#workspace-feeds).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateFeedBody): One feed to connect, with a sign-in when it is members-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Feed]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateFeedBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | Feed | None:
    """Connect a feed

     Connect an RSS or Atom feed, or a page advertising one, for the workspace's keywords to read hourly.

    - Idempotent: a feed already read returns 200.
    - A members-only forum answers `feed_login_required`: resend with `auth`.

    See [RSS](/platforms/rss#workspace-feeds).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
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
            idempotency_key=idempotency_key,
        )
    ).parsed
