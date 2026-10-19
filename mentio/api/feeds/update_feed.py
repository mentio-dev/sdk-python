from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.feed import Feed
from ...models.update_feed_body import UpdateFeedBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateFeedBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/feeds/{id}".format(
            id=quote(str(id), safe=""),
        ),
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

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

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
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFeedBody,
) -> Response[ErrorResponse | Feed]:
    """Update a feed

     Rename a feed (title, null clears it), or set its sign-in for a members-only forum (auth: a cookie
    copied from your browser, or one header such as Discourse's Api-Key). A sign-in is checked by
    reading the feed with it, stored encrypted, sent to the feed's own site alone and never shown again;
    the feed is then read for this workspace alone. auth: null removes it.

    Args:
        id (str): Feed id (fd_...). Example: fd_abc123.
        body (UpdateFeedBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Feed]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFeedBody,
) -> ErrorResponse | Feed | None:
    """Update a feed

     Rename a feed (title, null clears it), or set its sign-in for a members-only forum (auth: a cookie
    copied from your browser, or one header such as Discourse's Api-Key). A sign-in is checked by
    reading the feed with it, stored encrypted, sent to the feed's own site alone and never shown again;
    the feed is then read for this workspace alone. auth: null removes it.

    Args:
        id (str): Feed id (fd_...). Example: fd_abc123.
        body (UpdateFeedBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Feed
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFeedBody,
) -> Response[ErrorResponse | Feed]:
    """Update a feed

     Rename a feed (title, null clears it), or set its sign-in for a members-only forum (auth: a cookie
    copied from your browser, or one header such as Discourse's Api-Key). A sign-in is checked by
    reading the feed with it, stored encrypted, sent to the feed's own site alone and never shown again;
    the feed is then read for this workspace alone. auth: null removes it.

    Args:
        id (str): Feed id (fd_...). Example: fd_abc123.
        body (UpdateFeedBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Feed]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFeedBody,
) -> ErrorResponse | Feed | None:
    """Update a feed

     Rename a feed (title, null clears it), or set its sign-in for a members-only forum (auth: a cookie
    copied from your browser, or one header such as Discourse's Api-Key). A sign-in is checked by
    reading the feed with it, stored encrypted, sent to the feed's own site alone and never shown again;
    the feed is then read for this workspace alone. auth: null removes it.

    Args:
        id (str): Feed id (fd_...). Example: fd_abc123.
        body (UpdateFeedBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Feed
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
