from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.import_feeds_body import ImportFeedsBody
from ...models.import_feeds_response_200 import ImportFeedsResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: ImportFeedsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/feeds/import",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ImportFeedsResponse200 | None:
    if response.status_code == 200:
        response_200 = ImportFeedsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ImportFeedsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ImportFeedsBody,
) -> Response[ErrorResponse | ImportFeedsResponse200]:
    """Connect many feeds

     Connect up to 100 feeds in one call, each { url } or { url, auth } for a members-only one, checked
    on its own and reported added, already or failed, in the order sent: one that fails never stops the
    others. A failure carries the error code POST /v1/feeds would answer for that address
    (feed_login_required: send it again with auth). Every keyword of the workspace with
    readsWorkspaceFeeds (the default) reads these feeds: an item holding its term is one of its
    mentions, with its matching rules, billed like any mention. Each feed is read every hour; reading it
    is free. At most 500 a workspace. The first 8 added bring each reading keyword the newest 10
    matching items of the last 30 days; the rest start from now.

    Args:
        body (ImportFeedsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportFeedsResponse200]
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
    body: ImportFeedsBody,
) -> ErrorResponse | ImportFeedsResponse200 | None:
    """Connect many feeds

     Connect up to 100 feeds in one call, each { url } or { url, auth } for a members-only one, checked
    on its own and reported added, already or failed, in the order sent: one that fails never stops the
    others. A failure carries the error code POST /v1/feeds would answer for that address
    (feed_login_required: send it again with auth). Every keyword of the workspace with
    readsWorkspaceFeeds (the default) reads these feeds: an item holding its term is one of its
    mentions, with its matching rules, billed like any mention. Each feed is read every hour; reading it
    is free. At most 500 a workspace. The first 8 added bring each reading keyword the newest 10
    matching items of the last 30 days; the rest start from now.

    Args:
        body (ImportFeedsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportFeedsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ImportFeedsBody,
) -> Response[ErrorResponse | ImportFeedsResponse200]:
    """Connect many feeds

     Connect up to 100 feeds in one call, each { url } or { url, auth } for a members-only one, checked
    on its own and reported added, already or failed, in the order sent: one that fails never stops the
    others. A failure carries the error code POST /v1/feeds would answer for that address
    (feed_login_required: send it again with auth). Every keyword of the workspace with
    readsWorkspaceFeeds (the default) reads these feeds: an item holding its term is one of its
    mentions, with its matching rules, billed like any mention. Each feed is read every hour; reading it
    is free. At most 500 a workspace. The first 8 added bring each reading keyword the newest 10
    matching items of the last 30 days; the rest start from now.

    Args:
        body (ImportFeedsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportFeedsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ImportFeedsBody,
) -> ErrorResponse | ImportFeedsResponse200 | None:
    """Connect many feeds

     Connect up to 100 feeds in one call, each { url } or { url, auth } for a members-only one, checked
    on its own and reported added, already or failed, in the order sent: one that fails never stops the
    others. A failure carries the error code POST /v1/feeds would answer for that address
    (feed_login_required: send it again with auth). Every keyword of the workspace with
    readsWorkspaceFeeds (the default) reads these feeds: an item holding its term is one of its
    mentions, with its matching rules, billed like any mention. Each feed is read every hour; reading it
    is free. At most 500 a workspace. The first 8 added bring each reading keyword the newest 10
    matching items of the last 30 days; the rest start from now.

    Args:
        body (ImportFeedsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportFeedsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
