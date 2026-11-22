from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_accounts_response_200 import ListAccountsResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/accounts",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListAccountsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAccountsResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | ListAccountsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ListAccountsResponse200]:
    """List tracked accounts

     The accounts the workspace tracks for new followers, newest first.

    Each carries its follower count, the new followers billed this month and the poll state. An account
    costs $2 a month, a new follower $0.008. See [Followers](/guides/followers).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAccountsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ListAccountsResponse200 | None:
    """List tracked accounts

     The accounts the workspace tracks for new followers, newest first.

    Each carries its follower count, the new followers billed this month and the poll state. An account
    costs $2 a month, a new follower $0.008. See [Followers](/guides/followers).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAccountsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ListAccountsResponse200]:
    """List tracked accounts

     The accounts the workspace tracks for new followers, newest first.

    Each carries its follower count, the new followers billed this month and the poll state. An account
    costs $2 a month, a new follower $0.008. See [Followers](/guides/followers).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAccountsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ListAccountsResponse200 | None:
    """List tracked accounts

     The accounts the workspace tracks for new followers, newest first.

    Each carries its follower count, the new followers billed this month and the poll state. An account
    costs $2 a month, a new follower $0.008. See [Followers](/guides/followers).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAccountsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
