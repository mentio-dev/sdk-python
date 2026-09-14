from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_keyword_body import CreateKeywordBody
from ...models.error_response import ErrorResponse
from ...models.keyword import Keyword
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKeywordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/keywords",
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

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

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
    *,
    client: AuthenticatedClient,
    body: CreateKeywordBody,
) -> Response[ErrorResponse | Keyword]:
    """Track a keyword

     Start tracking a word or phrase. Matching, classification and delivery begin on the next poll. A
    funded workspace tracks up to 500 keywords; each costs $5 per month, deducted daily from the
    balance.

    Args:
        body (CreateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Keyword]
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
    body: CreateKeywordBody,
) -> ErrorResponse | Keyword | None:
    """Track a keyword

     Start tracking a word or phrase. Matching, classification and delivery begin on the next poll. A
    funded workspace tracks up to 500 keywords; each costs $5 per month, deducted daily from the
    balance.

    Args:
        body (CreateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Keyword
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKeywordBody,
) -> Response[ErrorResponse | Keyword]:
    """Track a keyword

     Start tracking a word or phrase. Matching, classification and delivery begin on the next poll. A
    funded workspace tracks up to 500 keywords; each costs $5 per month, deducted daily from the
    balance.

    Args:
        body (CreateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Keyword]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateKeywordBody,
) -> ErrorResponse | Keyword | None:
    """Track a keyword

     Start tracking a word or phrase. Matching, classification and delivery begin on the next poll. A
    funded workspace tracks up to 500 keywords; each costs $5 per month, deducted daily from the
    balance.

    Args:
        body (CreateKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Keyword
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
