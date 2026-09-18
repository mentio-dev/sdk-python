from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.whoami import Whoami
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/whoami",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Whoami | None:
    if response.status_code == 200:
        response_200 = Whoami.from_dict(response.json())

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
) -> Response[ErrorResponse | Whoami]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | Whoami]:
    """Introspect the credential

     The workspace this credential acts on, how the request authenticated (an API key, an OAuth access
    token from an MCP sign-in, or the dashboard session), whether it may write, and for a key its id and
    expiry. Run it first: a read key answers 403 read_only_key on every write, and a wrong workspace is
    the classic scripting mistake.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Whoami]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | Whoami | None:
    """Introspect the credential

     The workspace this credential acts on, how the request authenticated (an API key, an OAuth access
    token from an MCP sign-in, or the dashboard session), whether it may write, and for a key its id and
    expiry. Run it first: a read key answers 403 read_only_key on every write, and a wrong workspace is
    the classic scripting mistake.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Whoami
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | Whoami]:
    """Introspect the credential

     The workspace this credential acts on, how the request authenticated (an API key, an OAuth access
    token from an MCP sign-in, or the dashboard session), whether it may write, and for a key its id and
    expiry. Run it first: a read key answers 403 read_only_key on every write, and a wrong workspace is
    the classic scripting mistake.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Whoami]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | Whoami | None:
    """Introspect the credential

     The workspace this credential acts on, how the request authenticated (an API key, an OAuth access
    token from an MCP sign-in, or the dashboard session), whether it may write, and for a key its id and
    expiry. Run it first: a read key answers 403 read_only_key on every write, and a wrong workspace is
    the classic scripting mistake.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Whoami
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
