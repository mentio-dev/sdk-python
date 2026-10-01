from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_keyword_health_range import GetKeywordHealthRange
from ...models.keyword_health import KeywordHealth
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["ai"] = ai

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/keywords/{id}/health".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | KeywordHealth | None:
    if response.status_code == 200:
        response_200 = KeywordHealth.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | KeywordHealth]:
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
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> Response[ErrorResponse | KeywordHealth]:
    """Get a keyword's health

     Whether the keyword earns what it costs over a trailing window (`range`, default 30d): a status
    (healthy, noisy, quiet, capped, paused, new) with the reasons in plain words, its numbers by
    platform and week, what it cost, the words and authors its noise is made of, and suggestions. Each
    suggestion carries a `patch` to send to PATCH /v1/keywords/{id} as is, and the effect it would have
    had, measured by running the matcher's own rules over the window's posts. `ai=true` adds a context
    rewritten by a language model (cached a day, at most 20 model calls an hour per workspace). Read
    only and never billed; the report is cached for 5 minutes, and a change to the keyword starts a
    fresh one. At most 30 reads a minute per workspace.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): Trailing window of UTC days ending today, by match
            time: 7d, 30d, 90d (default 30d).
        ai (bool | Unset): true: also ask a language model for a rewritten context (cached a day
            per keyword and window, at most 20 model calls an hour per workspace). Default false:
            every suggestion comes from the rules alone.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordHealth]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        ai=ai,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> ErrorResponse | KeywordHealth | None:
    """Get a keyword's health

     Whether the keyword earns what it costs over a trailing window (`range`, default 30d): a status
    (healthy, noisy, quiet, capped, paused, new) with the reasons in plain words, its numbers by
    platform and week, what it cost, the words and authors its noise is made of, and suggestions. Each
    suggestion carries a `patch` to send to PATCH /v1/keywords/{id} as is, and the effect it would have
    had, measured by running the matcher's own rules over the window's posts. `ai=true` adds a context
    rewritten by a language model (cached a day, at most 20 model calls an hour per workspace). Read
    only and never billed; the report is cached for 5 minutes, and a change to the keyword starts a
    fresh one. At most 30 reads a minute per workspace.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): Trailing window of UTC days ending today, by match
            time: 7d, 30d, 90d (default 30d).
        ai (bool | Unset): true: also ask a language model for a rewritten context (cached a day
            per keyword and window, at most 20 model calls an hour per workspace). Default false:
            every suggestion comes from the rules alone.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordHealth
    """

    return sync_detailed(
        id=id,
        client=client,
        range_=range_,
        ai=ai,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> Response[ErrorResponse | KeywordHealth]:
    """Get a keyword's health

     Whether the keyword earns what it costs over a trailing window (`range`, default 30d): a status
    (healthy, noisy, quiet, capped, paused, new) with the reasons in plain words, its numbers by
    platform and week, what it cost, the words and authors its noise is made of, and suggestions. Each
    suggestion carries a `patch` to send to PATCH /v1/keywords/{id} as is, and the effect it would have
    had, measured by running the matcher's own rules over the window's posts. `ai=true` adds a context
    rewritten by a language model (cached a day, at most 20 model calls an hour per workspace). Read
    only and never billed; the report is cached for 5 minutes, and a change to the keyword starts a
    fresh one. At most 30 reads a minute per workspace.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): Trailing window of UTC days ending today, by match
            time: 7d, 30d, 90d (default 30d).
        ai (bool | Unset): true: also ask a language model for a rewritten context (cached a day
            per keyword and window, at most 20 model calls an hour per workspace). Default false:
            every suggestion comes from the rules alone.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordHealth]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        ai=ai,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> ErrorResponse | KeywordHealth | None:
    """Get a keyword's health

     Whether the keyword earns what it costs over a trailing window (`range`, default 30d): a status
    (healthy, noisy, quiet, capped, paused, new) with the reasons in plain words, its numbers by
    platform and week, what it cost, the words and authors its noise is made of, and suggestions. Each
    suggestion carries a `patch` to send to PATCH /v1/keywords/{id} as is, and the effect it would have
    had, measured by running the matcher's own rules over the window's posts. `ai=true` adds a context
    rewritten by a language model (cached a day, at most 20 model calls an hour per workspace). Read
    only and never billed; the report is cached for 5 minutes, and a change to the keyword starts a
    fresh one. At most 30 reads a minute per workspace.

    Args:
        id (str): Keyword id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): Trailing window of UTC days ending today, by match
            time: 7d, 30d, 90d (default 30d).
        ai (bool | Unset): true: also ask a language model for a rewritten context (cached a day
            per keyword and window, at most 20 model calls an hour per workspace). Default false:
            every suggestion comes from the rules alone.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordHealth
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            range_=range_,
            ai=ai,
        )
    ).parsed
