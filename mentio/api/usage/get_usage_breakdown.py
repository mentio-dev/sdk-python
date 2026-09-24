from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_usage_breakdown_by import GetUsageBreakdownBy
from ...models.get_usage_breakdown_range import GetUsageBreakdownRange
from ...models.usage_breakdown import UsageBreakdown
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_by: str | Unset = UNSET
    if not isinstance(by, Unset):
        json_by = by.value

    params["by"] = json_by

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["month"] = month

    params["limit"] = limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/breakdown",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | UsageBreakdown | None:
    if response.status_code == 200:
        response_200 = UsageBreakdown.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | UsageBreakdown]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | UsageBreakdown]:
    """Get the usage breakdown

     What the workspace consumed and was charged over a window, grouped by one dimension per call (`by`:
    day, platform or keyword), in USD cents at list price, with the window's totals on every call.
    `range` reads a trailing window of UTC days ending today (default 30d); `month` reads one calendar
    month (YYYY-MM), the shape a bill or a per-customer margin is reconciled against. Keyword-days come
    from the daily tick and mention charges from the matches that billed, so a deleted keyword keeps its
    charges in the keyword rows (`keyword.removed`) while its mention counts read 0; the same numbers
    ride on each keyword as `stats.cost` for the running month. `totals.ledgerDebitCents` is what the
    wallet has debited so far for the window's days: mentions settle the morning after their day, so a
    window ending today lags `totals.totalCents` by the unsettled ones, and a closed month differs from
    it only by cumulative rounding. Rows are paged (`limit`, `offset`, `total`); a workspace may read
    this at most 30 times a minute through its keys and tokens together.

    Args:
        by (GetUsageBreakdownBy | Unset): The dimension to group by: day (one row per UTC day of
            the window), platform, or keyword (default: the row a margin is computed from). Default:
            GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): Trailing window of UTC days ending today: 7d,
            30d, 90d (default 30d). Ignored when `month` is given.
        month (str | Unset): A calendar month (YYYY-MM, UTC) instead of a trailing window: from
            its first day to its last, or to today for the running month. A future month is a 400.
        limit (int | Unset): Rows per page, 1 to 500 (default 100). Only by=keyword can outgrow a
            page; a window has at most 90 days and a dozen platforms. Default: 100.
        offset (int | None | Unset): Skip this many rows. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UsageBreakdown]
    """

    kwargs = _get_kwargs(
        by=by,
        range_=range_,
        month=month,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> ErrorResponse | UsageBreakdown | None:
    """Get the usage breakdown

     What the workspace consumed and was charged over a window, grouped by one dimension per call (`by`:
    day, platform or keyword), in USD cents at list price, with the window's totals on every call.
    `range` reads a trailing window of UTC days ending today (default 30d); `month` reads one calendar
    month (YYYY-MM), the shape a bill or a per-customer margin is reconciled against. Keyword-days come
    from the daily tick and mention charges from the matches that billed, so a deleted keyword keeps its
    charges in the keyword rows (`keyword.removed`) while its mention counts read 0; the same numbers
    ride on each keyword as `stats.cost` for the running month. `totals.ledgerDebitCents` is what the
    wallet has debited so far for the window's days: mentions settle the morning after their day, so a
    window ending today lags `totals.totalCents` by the unsettled ones, and a closed month differs from
    it only by cumulative rounding. Rows are paged (`limit`, `offset`, `total`); a workspace may read
    this at most 30 times a minute through its keys and tokens together.

    Args:
        by (GetUsageBreakdownBy | Unset): The dimension to group by: day (one row per UTC day of
            the window), platform, or keyword (default: the row a margin is computed from). Default:
            GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): Trailing window of UTC days ending today: 7d,
            30d, 90d (default 30d). Ignored when `month` is given.
        month (str | Unset): A calendar month (YYYY-MM, UTC) instead of a trailing window: from
            its first day to its last, or to today for the running month. A future month is a 400.
        limit (int | Unset): Rows per page, 1 to 500 (default 100). Only by=keyword can outgrow a
            page; a window has at most 90 days and a dozen platforms. Default: 100.
        offset (int | None | Unset): Skip this many rows. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UsageBreakdown
    """

    return sync_detailed(
        client=client,
        by=by,
        range_=range_,
        month=month,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | UsageBreakdown]:
    """Get the usage breakdown

     What the workspace consumed and was charged over a window, grouped by one dimension per call (`by`:
    day, platform or keyword), in USD cents at list price, with the window's totals on every call.
    `range` reads a trailing window of UTC days ending today (default 30d); `month` reads one calendar
    month (YYYY-MM), the shape a bill or a per-customer margin is reconciled against. Keyword-days come
    from the daily tick and mention charges from the matches that billed, so a deleted keyword keeps its
    charges in the keyword rows (`keyword.removed`) while its mention counts read 0; the same numbers
    ride on each keyword as `stats.cost` for the running month. `totals.ledgerDebitCents` is what the
    wallet has debited so far for the window's days: mentions settle the morning after their day, so a
    window ending today lags `totals.totalCents` by the unsettled ones, and a closed month differs from
    it only by cumulative rounding. Rows are paged (`limit`, `offset`, `total`); a workspace may read
    this at most 30 times a minute through its keys and tokens together.

    Args:
        by (GetUsageBreakdownBy | Unset): The dimension to group by: day (one row per UTC day of
            the window), platform, or keyword (default: the row a margin is computed from). Default:
            GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): Trailing window of UTC days ending today: 7d,
            30d, 90d (default 30d). Ignored when `month` is given.
        month (str | Unset): A calendar month (YYYY-MM, UTC) instead of a trailing window: from
            its first day to its last, or to today for the running month. A future month is a 400.
        limit (int | Unset): Rows per page, 1 to 500 (default 100). Only by=keyword can outgrow a
            page; a window has at most 90 days and a dozen platforms. Default: 100.
        offset (int | None | Unset): Skip this many rows. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UsageBreakdown]
    """

    kwargs = _get_kwargs(
        by=by,
        range_=range_,
        month=month,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> ErrorResponse | UsageBreakdown | None:
    """Get the usage breakdown

     What the workspace consumed and was charged over a window, grouped by one dimension per call (`by`:
    day, platform or keyword), in USD cents at list price, with the window's totals on every call.
    `range` reads a trailing window of UTC days ending today (default 30d); `month` reads one calendar
    month (YYYY-MM), the shape a bill or a per-customer margin is reconciled against. Keyword-days come
    from the daily tick and mention charges from the matches that billed, so a deleted keyword keeps its
    charges in the keyword rows (`keyword.removed`) while its mention counts read 0; the same numbers
    ride on each keyword as `stats.cost` for the running month. `totals.ledgerDebitCents` is what the
    wallet has debited so far for the window's days: mentions settle the morning after their day, so a
    window ending today lags `totals.totalCents` by the unsettled ones, and a closed month differs from
    it only by cumulative rounding. Rows are paged (`limit`, `offset`, `total`); a workspace may read
    this at most 30 times a minute through its keys and tokens together.

    Args:
        by (GetUsageBreakdownBy | Unset): The dimension to group by: day (one row per UTC day of
            the window), platform, or keyword (default: the row a margin is computed from). Default:
            GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): Trailing window of UTC days ending today: 7d,
            30d, 90d (default 30d). Ignored when `month` is given.
        month (str | Unset): A calendar month (YYYY-MM, UTC) instead of a trailing window: from
            its first day to its last, or to today for the running month. A future month is a 400.
        limit (int | Unset): Rows per page, 1 to 500 (default 100). Only by=keyword can outgrow a
            page; a window has at most 90 days and a dozen platforms. Default: 100.
        offset (int | None | Unset): Skip this many rows. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UsageBreakdown
    """

    return (
        await asyncio_detailed(
            client=client,
            by=by,
            range_=range_,
            month=month,
            limit=limit,
            offset=offset,
        )
    ).parsed
