from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.keyword_deletion_preview import KeywordDeletionPreview
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/keywords/{id}/deletion-preview".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | KeywordDeletionPreview | None:
    if response.status_code == 200:
        response_200 = KeywordDeletionPreview.from_dict(response.json())

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
) -> Response[ErrorResponse | KeywordDeletionPreview]:
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
) -> Response[ErrorResponse | KeywordDeletionPreview]:
    """Preview a keyword deletion

     What DELETE /v1/keywords/{id} would remove or change, without changing anything.

    - Its mentions and what it cost this month (charges already made stay).
    - Alert rules, automations and views naming it, and the effect on each: disabled, narrowed or empty.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordDeletionPreview]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | KeywordDeletionPreview | None:
    """Preview a keyword deletion

     What DELETE /v1/keywords/{id} would remove or change, without changing anything.

    - Its mentions and what it cost this month (charges already made stay).
    - Alert rules, automations and views naming it, and the effect on each: disabled, narrowed or empty.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordDeletionPreview
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | KeywordDeletionPreview]:
    """Preview a keyword deletion

     What DELETE /v1/keywords/{id} would remove or change, without changing anything.

    - Its mentions and what it cost this month (charges already made stay).
    - Alert rules, automations and views naming it, and the effect on each: disabled, narrowed or empty.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordDeletionPreview]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | KeywordDeletionPreview | None:
    """Preview a keyword deletion

     What DELETE /v1/keywords/{id} would remove or change, without changing anything.

    - Its mentions and what it cost this month (charges already made stay).
    - Alert rules, automations and views naming it, and the effect on each: disabled, narrowed or empty.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordDeletionPreview
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
