from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.duplicate_keyword_body import DuplicateKeywordBody
from ...models.error_response import ErrorResponse
from ...models.keyword import Keyword
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: DuplicateKeywordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

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
) -> Response[ErrorResponse | Keyword]:
    """Duplicate a keyword

     A new keyword with this one's settings and a new `term` (or the same term in another group): its
    kind, platforms, context, every matching rule, its monthly mention cap and its comments setting.
    Review apps and feeds are copied only when listed in `include`. It is a new keyword: $5 per month,
    and the newest posts of the last 30 days come in at once, as with any new keyword.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
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
) -> ErrorResponse | Keyword | None:
    """Duplicate a keyword

     A new keyword with this one's settings and a new `term` (or the same term in another group): its
    kind, platforms, context, every matching rule, its monthly mention cap and its comments setting.
    Review apps and feeds are copied only when listed in `include`. It is a new keyword: $5 per month,
    and the newest posts of the last 30 days come in at once, as with any new keyword.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
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
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: DuplicateKeywordBody,
) -> Response[ErrorResponse | Keyword]:
    """Duplicate a keyword

     A new keyword with this one's settings and a new `term` (or the same term in another group): its
    kind, platforms, context, every matching rule, its monthly mention cap and its comments setting.
    Review apps and feeds are copied only when listed in `include`. It is a new keyword: $5 per month,
    and the newest posts of the last 30 days come in at once, as with any new keyword.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: DuplicateKeywordBody,
) -> ErrorResponse | Keyword | None:
    """Duplicate a keyword

     A new keyword with this one's settings and a new `term` (or the same term in another group): its
    kind, platforms, context, every matching rule, its monthly mention cap and its comments setting.
    Review apps and feeds are copied only when listed in `include`. It is a new keyword: $5 per month,
    and the newest posts of the last 30 days come in at once, as with any new keyword.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
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
        )
    ).parsed
