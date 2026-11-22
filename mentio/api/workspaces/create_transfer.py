from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_transfer_body import CreateTransferBody
from ...models.error_response import ErrorResponse
from ...models.transfer import Transfer
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: CreateTransferBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workspaces/{id}/transfers".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Transfer | None:
    if response.status_code == 201:
        response_201 = Transfer.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Transfer]:
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
    body: CreateTransferBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | Transfer]:
    """Move money to or from a child workspace

     Moves USD cents between your balance and the child's, one ledger row on each side. The payer's
    effective balance must cover it; a transfer in counts against the child's monthly limit. Nothing
    charges a card or pays out. See [Agency workspaces](/guides/agency-workspaces#fund-a-child).

    Args:
        id (str): Child workspace id (org_...). Example: org_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Transfer]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateTransferBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | Transfer | None:
    """Move money to or from a child workspace

     Moves USD cents between your balance and the child's, one ledger row on each side. The payer's
    effective balance must cover it; a transfer in counts against the child's monthly limit. Nothing
    charges a card or pays out. See [Agency workspaces](/guides/agency-workspaces#fund-a-child).

    Args:
        id (str): Child workspace id (org_...). Example: org_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Transfer
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateTransferBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | Transfer]:
    """Move money to or from a child workspace

     Moves USD cents between your balance and the child's, one ledger row on each side. The payer's
    effective balance must cover it; a transfer in counts against the child's monthly limit. Nothing
    charges a card or pays out. See [Agency workspaces](/guides/agency-workspaces#fund-a-child).

    Args:
        id (str): Child workspace id (org_...). Example: org_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Transfer]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateTransferBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | Transfer | None:
    """Move money to or from a child workspace

     Moves USD cents between your balance and the child's, one ledger row on each side. The payer's
    effective balance must cover it; a transfer in counts against the child's monthly limit. Nothing
    charges a card or pays out. See [Agency workspaces](/guides/agency-workspaces#fund-a-child).

    Args:
        id (str): Child workspace id (org_...). Example: org_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Transfer
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
