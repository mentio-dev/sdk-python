from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_email_channel import CreateEmailChannel
from ...models.create_slack_channel import CreateSlackChannel
from ...models.create_webhook_channel import CreateWebhookChannel
from ...models.email_channel import EmailChannel
from ...models.error_response import ErrorResponse
from ...models.slack_channel import SlackChannel
from ...models.telegram_channel import TelegramChannel
from ...models.webhook_channel import WebhookChannel
from ...types import Response


def _get_kwargs(
    *,
    body: CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels",
    }

    if isinstance(body, CreateSlackChannel) or isinstance(body, CreateEmailChannel):
        _kwargs["json"] = body.to_dict()
    else:
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
    if response.status_code == 201:

        def _parse_response_201(
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

        response_201 = _parse_response_201(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

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
    *,
    client: AuthenticatedClient,
    body: CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel,
) -> Response[
    EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
]:
    """Create a channel

    Args:
        body (CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse]
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
    body: CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel,
) -> (
    EmailChannel
    | SlackChannel
    | TelegramChannel
    | WebhookChannel
    | ErrorResponse
    | None
):
    """Create a channel

    Args:
        body (CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel,
) -> Response[
    EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
]:
    """Create a channel

    Args:
        body (CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel,
) -> (
    EmailChannel
    | SlackChannel
    | TelegramChannel
    | WebhookChannel
    | ErrorResponse
    | None
):
    """Create a channel

    Args:
        body (CreateEmailChannel | CreateSlackChannel | CreateWebhookChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailChannel | SlackChannel | TelegramChannel | WebhookChannel | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
