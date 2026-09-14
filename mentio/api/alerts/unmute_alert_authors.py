from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert import Alert
from ...models.error_response import ErrorResponse
from ...models.unmute_alert_authors_body import UnmuteAlertAuthorsBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UnmuteAlertAuthorsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/alerts/{id}/unmute".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Alert | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = Alert.from_dict(response.json())

        return response_200

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
) -> Response[Alert | ErrorResponse]:
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
    body: UnmuteAlertAuthorsBody,
) -> Response[Alert | ErrorResponse]:
    """Unmute authors on an alert

     Remove authors from the alert's muted list without touching the rest of its filter. Name each one by
    the stored entry or by any link to that profile or its posts. Authors that are not muted are
    ignored, so a retry is safe.

    Args:
        id (str): Alert id (feed_...). Example: feed_abc123.
        body (UnmuteAlertAuthorsBody): Authors to add to or remove from the alert's muted list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert | ErrorResponse]
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
    body: UnmuteAlertAuthorsBody,
) -> Alert | ErrorResponse | None:
    """Unmute authors on an alert

     Remove authors from the alert's muted list without touching the rest of its filter. Name each one by
    the stored entry or by any link to that profile or its posts. Authors that are not muted are
    ignored, so a retry is safe.

    Args:
        id (str): Alert id (feed_...). Example: feed_abc123.
        body (UnmuteAlertAuthorsBody): Authors to add to or remove from the alert's muted list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert | ErrorResponse
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
    body: UnmuteAlertAuthorsBody,
) -> Response[Alert | ErrorResponse]:
    """Unmute authors on an alert

     Remove authors from the alert's muted list without touching the rest of its filter. Name each one by
    the stored entry or by any link to that profile or its posts. Authors that are not muted are
    ignored, so a retry is safe.

    Args:
        id (str): Alert id (feed_...). Example: feed_abc123.
        body (UnmuteAlertAuthorsBody): Authors to add to or remove from the alert's muted list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert | ErrorResponse]
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
    body: UnmuteAlertAuthorsBody,
) -> Alert | ErrorResponse | None:
    """Unmute authors on an alert

     Remove authors from the alert's muted list without touching the rest of its filter. Name each one by
    the stored entry or by any link to that profile or its posts. Authors that are not muted are
    ignored, so a retry is safe.

    Args:
        id (str): Alert id (feed_...). Example: feed_abc123.
        body (UnmuteAlertAuthorsBody): Authors to add to or remove from the alert's muted list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
