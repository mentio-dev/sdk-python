from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_series import AnalyticsSeries
from ...models.error_response import ErrorResponse
from ...models.get_analytics_series_bucket import GetAnalyticsSeriesBucket
from ...models.get_analytics_series_by import GetAnalyticsSeriesBy
from ...models.get_analytics_series_platforms_item import (
    GetAnalyticsSeriesPlatformsItem,
)
from ...models.get_analytics_series_range import GetAnalyticsSeriesRange
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    range_: GetAnalyticsSeriesRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsSeriesPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetAnalyticsSeriesBucket | Unset = UNSET,
    by: GetAnalyticsSeriesBy | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["from"] = from_

    params["to"] = to

    json_keyword_ids: list[str] | None | Unset
    if isinstance(keyword_ids, Unset):
        json_keyword_ids = UNSET
    elif isinstance(keyword_ids, list):
        json_keyword_ids = keyword_ids

    else:
        json_keyword_ids = keyword_ids
    params["keywordIds"] = json_keyword_ids

    json_platforms: list[str] | Unset = UNSET
    if not isinstance(platforms, Unset):
        json_platforms = []
        for platforms_item_data in platforms:
            platforms_item = platforms_item_data.value
            json_platforms.append(platforms_item)

    params["platforms"] = json_platforms

    params["compare"] = compare

    params["timezone"] = timezone

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket.value

    params["bucket"] = json_bucket

    json_by: str | Unset = UNSET
    if not isinstance(by, Unset):
        json_by = by.value

    params["by"] = json_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsSeries | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AnalyticsSeries.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsSeries | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsSeriesRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsSeriesPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetAnalyticsSeriesBucket | Unset = UNSET,
    by: GetAnalyticsSeriesBy | Unset = UNSET,
) -> Response[AnalyticsSeries | ErrorResponse]:
    """Mentions over time

     Matched, relevant and sentiment counts per day or week across the window, as one total series or
    split per platform or per keyword with `by`. The window is `range` (7d, 30d, 90d, 365d, ending
    today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsSeriesRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsSeriesPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetAnalyticsSeriesBucket | Unset): Point granularity. Default: day up to 90 days,
            week beyond. Weeks start on Monday.
        by (GetAnalyticsSeriesBy | Unset): Split into one series per platform or per keyword (the
            top 20 by matched, the rest folded into "other"). Omit for one total series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSeries | ErrorResponse]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
        bucket=bucket,
        by=by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsSeriesRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsSeriesPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetAnalyticsSeriesBucket | Unset = UNSET,
    by: GetAnalyticsSeriesBy | Unset = UNSET,
) -> AnalyticsSeries | ErrorResponse | None:
    """Mentions over time

     Matched, relevant and sentiment counts per day or week across the window, as one total series or
    split per platform or per keyword with `by`. The window is `range` (7d, 30d, 90d, 365d, ending
    today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsSeriesRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsSeriesPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetAnalyticsSeriesBucket | Unset): Point granularity. Default: day up to 90 days,
            week beyond. Weeks start on Monday.
        by (GetAnalyticsSeriesBy | Unset): Split into one series per platform or per keyword (the
            top 20 by matched, the rest folded into "other"). Omit for one total series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSeries | ErrorResponse
    """

    return sync_detailed(
        client=client,
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
        bucket=bucket,
        by=by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsSeriesRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsSeriesPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetAnalyticsSeriesBucket | Unset = UNSET,
    by: GetAnalyticsSeriesBy | Unset = UNSET,
) -> Response[AnalyticsSeries | ErrorResponse]:
    """Mentions over time

     Matched, relevant and sentiment counts per day or week across the window, as one total series or
    split per platform or per keyword with `by`. The window is `range` (7d, 30d, 90d, 365d, ending
    today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsSeriesRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsSeriesPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetAnalyticsSeriesBucket | Unset): Point granularity. Default: day up to 90 days,
            week beyond. Weeks start on Monday.
        by (GetAnalyticsSeriesBy | Unset): Split into one series per platform or per keyword (the
            top 20 by matched, the rest folded into "other"). Omit for one total series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSeries | ErrorResponse]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
        bucket=bucket,
        by=by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsSeriesRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsSeriesPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetAnalyticsSeriesBucket | Unset = UNSET,
    by: GetAnalyticsSeriesBy | Unset = UNSET,
) -> AnalyticsSeries | ErrorResponse | None:
    """Mentions over time

     Matched, relevant and sentiment counts per day or week across the window, as one total series or
    split per platform or per keyword with `by`. The window is `range` (7d, 30d, 90d, 365d, ending
    today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsSeriesRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsSeriesPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetAnalyticsSeriesBucket | Unset): Point granularity. Default: day up to 90 days,
            week beyond. Weeks start on Monday.
        by (GetAnalyticsSeriesBy | Unset): Split into one series per platform or per keyword (the
            top 20 by matched, the rest folded into "other"). Omit for one total series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSeries | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            range_=range_,
            from_=from_,
            to=to,
            keyword_ids=keyword_ids,
            platforms=platforms,
            compare=compare,
            timezone=timezone,
            bucket=bucket,
            by=by,
        )
    ).parsed
