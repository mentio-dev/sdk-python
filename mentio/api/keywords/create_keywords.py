from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_keywords_body import CreateKeywordsBody
from ...models.error_response import ErrorResponse
from ...models.keyword_batch_result import KeywordBatchResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateKeywordsBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/keywords/batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | KeywordBatchResult | None:
    if response.status_code == 200:
        response_200 = KeywordBatchResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | KeywordBatchResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKeywordsBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | KeywordBatchResult]:
    """Track many keywords

     Create up to 100 keywords in one call, as POST /v1/keywords would, without reviewSources and feeds.

    - Each is created or refused on its own; `data` answers in order.
    - The wallet is checked keyword by keyword; none created for it is a 402.

    See [Keywords](/guides/keywords#add-many-at-once).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordBatchResult]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateKeywordsBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | KeywordBatchResult | None:
    """Track many keywords

     Create up to 100 keywords in one call, as POST /v1/keywords would, without reviewSources and feeds.

    - Each is created or refused on its own; `data` answers in order.
    - The wallet is checked keyword by keyword; none created for it is a 402.

    See [Keywords](/guides/keywords#add-many-at-once).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordBatchResult
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKeywordsBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | KeywordBatchResult]:
    """Track many keywords

     Create up to 100 keywords in one call, as POST /v1/keywords would, without reviewSources and feeds.

    - Each is created or refused on its own; `data` answers in order.
    - The wallet is checked keyword by keyword; none created for it is a 402.

    See [Keywords](/guides/keywords#add-many-at-once).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordBatchResult]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateKeywordsBody,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | KeywordBatchResult | None:
    """Track many keywords

     Create up to 100 keywords in one call, as POST /v1/keywords would, without reviewSources and feeds.

    - Each is created or refused on its own; `data` answers in order.
    - The wallet is checked keyword by keyword; none created for it is a 402.

    See [Keywords](/guides/keywords#add-many-at-once).

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordBatchResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
