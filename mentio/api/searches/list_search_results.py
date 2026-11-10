from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_search_results_response_200 import ListSearchResultsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_min_relevance: int | None | Unset
    if isinstance(min_relevance, Unset):
        json_min_relevance = UNSET
    else:
        json_min_relevance = min_relevance
    params["minRelevance"] = json_min_relevance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/searches/{id}/results".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListSearchResultsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListSearchResultsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ErrorResponse | ListSearchResultsResponse200]:
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
) -> Response[ErrorResponse | ListSearchResultsResponse200]:
    """List a search's results

     The posts the search found, newest first, with their verdicts.

    A verdict is null while it waits; `alreadyInWorkspace` says the post is already one of your
    mentions. Readable while the search runs.

    Args:
        id (str): Search id (srch_...). Example: srch_abc123.
        limit (int | Unset): Page size, 1 to 100. Default: 50.
        cursor (str | Unset): nextCursor from the previous page.
        min_relevance (int | None | Unset): Only results scored at least this relevant (0 to 100);
            unscored results are left out when set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListSearchResultsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        min_relevance=min_relevance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
) -> ErrorResponse | ListSearchResultsResponse200 | None:
    """List a search's results

     The posts the search found, newest first, with their verdicts.

    A verdict is null while it waits; `alreadyInWorkspace` says the post is already one of your
    mentions. Readable while the search runs.

    Args:
        id (str): Search id (srch_...). Example: srch_abc123.
        limit (int | Unset): Page size, 1 to 100. Default: 50.
        cursor (str | Unset): nextCursor from the previous page.
        min_relevance (int | None | Unset): Only results scored at least this relevant (0 to 100);
            unscored results are left out when set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListSearchResultsResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
        min_relevance=min_relevance,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
) -> Response[ErrorResponse | ListSearchResultsResponse200]:
    """List a search's results

     The posts the search found, newest first, with their verdicts.

    A verdict is null while it waits; `alreadyInWorkspace` says the post is already one of your
    mentions. Readable while the search runs.

    Args:
        id (str): Search id (srch_...). Example: srch_abc123.
        limit (int | Unset): Page size, 1 to 100. Default: 50.
        cursor (str | Unset): nextCursor from the previous page.
        min_relevance (int | None | Unset): Only results scored at least this relevant (0 to 100);
            unscored results are left out when set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListSearchResultsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        min_relevance=min_relevance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
) -> ErrorResponse | ListSearchResultsResponse200 | None:
    """List a search's results

     The posts the search found, newest first, with their verdicts.

    A verdict is null while it waits; `alreadyInWorkspace` says the post is already one of your
    mentions. Readable while the search runs.

    Args:
        id (str): Search id (srch_...). Example: srch_abc123.
        limit (int | Unset): Page size, 1 to 100. Default: 50.
        cursor (str | Unset): nextCursor from the previous page.
        min_relevance (int | None | Unset): Only results scored at least this relevant (0 to 100);
            unscored results are left out when set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListSearchResultsResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
            min_relevance=min_relevance,
        )
    ).parsed
