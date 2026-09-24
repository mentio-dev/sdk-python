from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.wallet import Wallet
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/wallet",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Wallet | None:
    if response.status_code == 200:
        response_200 = Wallet.from_dict(response.json())

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
) -> Response[ErrorResponse | Wallet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | Wallet]:
    """Get the wallet

     The prepaid balance in full: ledger, pending mention charges and the effective balance the stop rule
    reads, the daily burn and the days it buys, how many keywords run and how many the wallet paused,
    what a day costs and what a resume needs, the welcome credit, the newest top-up, the top-up bounds
    and the auto-recharge settings. `GET /v1/usage` is the short form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Wallet]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | Wallet | None:
    """Get the wallet

     The prepaid balance in full: ledger, pending mention charges and the effective balance the stop rule
    reads, the daily burn and the days it buys, how many keywords run and how many the wallet paused,
    what a day costs and what a resume needs, the welcome credit, the newest top-up, the top-up bounds
    and the auto-recharge settings. `GET /v1/usage` is the short form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Wallet
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | Wallet]:
    """Get the wallet

     The prepaid balance in full: ledger, pending mention charges and the effective balance the stop rule
    reads, the daily burn and the days it buys, how many keywords run and how many the wallet paused,
    what a day costs and what a resume needs, the welcome credit, the newest top-up, the top-up bounds
    and the auto-recharge settings. `GET /v1/usage` is the short form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Wallet]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | Wallet | None:
    """Get the wallet

     The prepaid balance in full: ledger, pending mention charges and the effective balance the stop rule
    reads, the daily burn and the days it buys, how many keywords run and how many the wallet paused,
    what a day costs and what a resume needs, the welcome credit, the newest top-up, the top-up bounds
    and the auto-recharge settings. `GET /v1/usage` is the short form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Wallet
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
