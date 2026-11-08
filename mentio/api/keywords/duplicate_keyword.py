from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.duplicate_keyword_body import DuplicateKeywordBody
from ...models.error_response import ErrorResponse
from ...models.keyword import Keyword
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: DuplicateKeywordBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/keywords/{id}/duplicate".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Keyword | None:
    if response.status_code == 201:
        response_201 = Keyword.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Keyword]:
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
    body: DuplicateKeywordBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | Keyword]:
    """Duplicate a keyword

     Create a keyword with this one's settings under a new term or group.

    It copies kind, platforms, context, rules, cap and comments; review apps and feeds only via
    `include`. A new keyword: $5 a month and a 30-day look-back.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (DuplicateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Keyword]
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
    body: DuplicateKeywordBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | Keyword | None:
    """Duplicate a keyword

     Create a keyword with this one's settings under a new term or group.

    It copies kind, platforms, context, rules, cap and comments; review apps and feeds only via
    `include`. A new keyword: $5 a month and a 30-day look-back.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (DuplicateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Keyword
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
    body: DuplicateKeywordBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | Keyword]:
    """Duplicate a keyword

     Create a keyword with this one's settings under a new term or group.

    It copies kind, platforms, context, rules, cap and comments; review apps and feeds only via
    `include`. A new keyword: $5 a month and a 30-day look-back.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (DuplicateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Keyword]
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
    body: DuplicateKeywordBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | Keyword | None:
    """Duplicate a keyword

     Create a keyword with this one's settings under a new term or group.

    It copies kind, platforms, context, rules, cap and comments; review apps and feeds only via
    `include`. A new keyword: $5 a month and a 30-day look-back.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (DuplicateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Keyword
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
