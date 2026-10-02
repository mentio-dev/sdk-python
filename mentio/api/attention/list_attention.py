from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_attention_response_200 import ListAttentionResponse200
from ...models.list_attention_status import ListAttentionStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["kind"] = kind

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/attention",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListAttentionResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAttentionResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | ListAttentionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | ListAttentionResponse200]:
    """List attention items

     What needs a person, newest first: a keyword whose mentions spiked in the last hour (mention.spike),
    whose negative share of the last 24 hours jumped (sentiment.negative_spike), that turned noisy
    (keyword.noisy), or a channel whose last sends all failed (channel.failing). Detected once an hour;
    an item opens when its condition starts and resolves on its own when the condition is gone. Open
    items by default; `status=all` reads the history. Each opening is also an account event of the same
    name, which webhook, Slack, email and Telegram channels can subscribe to.

    Args:
        status (ListAttentionStatus | Unset): open (default), resolved, dismissed, or all.
            Default: ListAttentionStatus.OPEN.
        kind (str | Unset): Only these kinds, comma separated: mention.spike,
            sentiment.negative_spike, keyword.noisy, channel.failing.
        limit (int | Unset): Items per page, newest first; 50 by default, at most 100. Default:
            50.
        cursor (str | Unset): nextCursor from the previous page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAttentionResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | ListAttentionResponse200 | None:
    """List attention items

     What needs a person, newest first: a keyword whose mentions spiked in the last hour (mention.spike),
    whose negative share of the last 24 hours jumped (sentiment.negative_spike), that turned noisy
    (keyword.noisy), or a channel whose last sends all failed (channel.failing). Detected once an hour;
    an item opens when its condition starts and resolves on its own when the condition is gone. Open
    items by default; `status=all` reads the history. Each opening is also an account event of the same
    name, which webhook, Slack, email and Telegram channels can subscribe to.

    Args:
        status (ListAttentionStatus | Unset): open (default), resolved, dismissed, or all.
            Default: ListAttentionStatus.OPEN.
        kind (str | Unset): Only these kinds, comma separated: mention.spike,
            sentiment.negative_spike, keyword.noisy, channel.failing.
        limit (int | Unset): Items per page, newest first; 50 by default, at most 100. Default:
            50.
        cursor (str | Unset): nextCursor from the previous page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAttentionResponse200
    """

    return sync_detailed(
        client=client,
        status=status,
        kind=kind,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | ListAttentionResponse200]:
    """List attention items

     What needs a person, newest first: a keyword whose mentions spiked in the last hour (mention.spike),
    whose negative share of the last 24 hours jumped (sentiment.negative_spike), that turned noisy
    (keyword.noisy), or a channel whose last sends all failed (channel.failing). Detected once an hour;
    an item opens when its condition starts and resolves on its own when the condition is gone. Open
    items by default; `status=all` reads the history. Each opening is also an account event of the same
    name, which webhook, Slack, email and Telegram channels can subscribe to.

    Args:
        status (ListAttentionStatus | Unset): open (default), resolved, dismissed, or all.
            Default: ListAttentionStatus.OPEN.
        kind (str | Unset): Only these kinds, comma separated: mention.spike,
            sentiment.negative_spike, keyword.noisy, channel.failing.
        limit (int | Unset): Items per page, newest first; 50 by default, at most 100. Default:
            50.
        cursor (str | Unset): nextCursor from the previous page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAttentionResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | ListAttentionResponse200 | None:
    """List attention items

     What needs a person, newest first: a keyword whose mentions spiked in the last hour (mention.spike),
    whose negative share of the last 24 hours jumped (sentiment.negative_spike), that turned noisy
    (keyword.noisy), or a channel whose last sends all failed (channel.failing). Detected once an hour;
    an item opens when its condition starts and resolves on its own when the condition is gone. Open
    items by default; `status=all` reads the history. Each opening is also an account event of the same
    name, which webhook, Slack, email and Telegram channels can subscribe to.

    Args:
        status (ListAttentionStatus | Unset): open (default), resolved, dismissed, or all.
            Default: ListAttentionStatus.OPEN.
        kind (str | Unset): Only these kinds, comma separated: mention.spike,
            sentiment.negative_spike, keyword.noisy, channel.failing.
        limit (int | Unset): Items per page, newest first; 50 by default, at most 100. Default:
            50.
        cursor (str | Unset): nextCursor from the previous page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAttentionResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            kind=kind,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
