from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_channel import EmailChannel
from ...models.error_response import ErrorResponse
from ...models.slack_channel import SlackChannel
from ...models.telegram_channel import TelegramChannel
from ...models.update_channel_body import UpdateChannelBody
from ...models.webhook_channel import WebhookChannel
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateChannelBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/channels/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EmailChannel
    | SlackChannel
    | TelegramChannel
    | WebhookChannel
    | ErrorResponse
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> EmailChannel | SlackChannel | TelegramChannel | WebhookChannel:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_channel_type_0 = SlackChannel.from_dict(data)

                return componentsschemas_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_channel_type_1 = EmailChannel.from_dict(data)

                return componentsschemas_channel_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_channel_type_2 = WebhookChannel.from_dict(data)

                return componentsschemas_channel_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_channel_type_3 = TelegramChannel.from_dict(data)

            return componentsschemas_channel_type_3

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
]:
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
    body: UpdateChannelBody,
) -> Response[
    EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
]:
    """Update a channel

    Args:
        id (str): Channel id (dest_...). Example: dest_abc123.
        body (UpdateChannelBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse]
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
    body: UpdateChannelBody,
) -> (
    EmailChannel
    | SlackChannel
    | TelegramChannel
    | WebhookChannel
    | ErrorResponse
    | None
):
    """Update a channel

    Args:
        id (str): Channel id (dest_...). Example: dest_abc123.
        body (UpdateChannelBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
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
    body: UpdateChannelBody,
) -> Response[
    EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
]:
    """Update a channel

    Args:
        id (str): Channel id (dest_...). Example: dest_abc123.
        body (UpdateChannelBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse]
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
    body: UpdateChannelBody,
) -> (
    EmailChannel
    | SlackChannel
    | TelegramChannel
    | WebhookChannel
    | ErrorResponse
    | None
):
    """Update a channel

    Args:
        id (str): Channel id (dest_...). Example: dest_abc123.
        body (UpdateChannelBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
