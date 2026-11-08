from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attention_item import AttentionItem
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/attention/{id}/dismiss".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttentionItem | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AttentionItem.from_dict(response.json())

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
) -> Response[AttentionItem | ErrorResponse]:
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
    idempotency_key: str | Unset = UNSET,
) -> Response[AttentionItem | ErrorResponse]:
    """Dismiss an attention item

     Put an attention item away. Idempotent.

    It leaves the open list and does not come back while its condition lasts. Once the condition clears,
    a new episode may open a new item.

    Args:
        id (str): Attention item id (att_...). Example: att_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttentionItem | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
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
    idempotency_key: str | Unset = UNSET,
) -> AttentionItem | ErrorResponse | None:
    """Dismiss an attention item

     Put an attention item away. Idempotent.

    It leaves the open list and does not come back while its condition lasts. Once the condition clears,
    a new episode may open a new item.

    Args:
        id (str): Attention item id (att_...). Example: att_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttentionItem | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[AttentionItem | ErrorResponse]:
    """Dismiss an attention item

     Put an attention item away. Idempotent.

    It leaves the open list and does not come back while its condition lasts. Once the condition clears,
    a new episode may open a new item.

    Args:
        id (str): Attention item id (att_...). Example: att_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttentionItem | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> AttentionItem | ErrorResponse | None:
    """Dismiss an attention item

     Put an attention item away. Idempotent.

    It leaves the open list and does not come back while its condition lasts. Once the condition clears,
    a new episode may open a new item.

    Args:
        id (str): Attention item id (att_...). Example: att_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttentionItem | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
