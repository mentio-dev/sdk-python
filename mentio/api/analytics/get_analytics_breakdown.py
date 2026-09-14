from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_breakdown import AnalyticsBreakdown
from ...models.error_response import ErrorResponse
from ...models.get_analytics_breakdown_by import GetAnalyticsBreakdownBy
from ...models.get_analytics_breakdown_platforms_item import (
    GetAnalyticsBreakdownPlatformsItem,
)
from ...models.get_analytics_breakdown_range import GetAnalyticsBreakdownRange
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    range_: GetAnalyticsBreakdownRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsBreakdownPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    by: GetAnalyticsBreakdownBy,
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

    json_by = by.value
    params["by"] = json_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/breakdown",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsBreakdown | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AnalyticsBreakdown.from_dict(response.json())

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
) -> Response[AnalyticsBreakdown | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsBreakdownRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsBreakdownPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    by: GetAnalyticsBreakdownBy,
) -> Response[AnalyticsBreakdown | ErrorResponse]:
    """Mentions grouped by one dimension

     One table of matched, relevant and sentiment counts grouped by `by`: platform, keyword, sentiment,
    intent, status, hour (weekday and hour of day) or person. The window is `range` (7d, 30d, 90d, 365d,
    ending today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsBreakdownRange | Unset): Preset window ending today. Ignored when from
            or to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsBreakdownPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        by (GetAnalyticsBreakdownBy): The dimension to group by: platform, keyword, sentiment
            (unclassified included), intent (a mention can carry several), status (open, ignored,
            done), hour (weekday and hour of day in `timezone`), person (who posted; anonymous posts
            are left out).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsBreakdown | ErrorResponse]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
        by=by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsBreakdownRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsBreakdownPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    by: GetAnalyticsBreakdownBy,
) -> AnalyticsBreakdown | ErrorResponse | None:
    """Mentions grouped by one dimension

     One table of matched, relevant and sentiment counts grouped by `by`: platform, keyword, sentiment,
    intent, status, hour (weekday and hour of day) or person. The window is `range` (7d, 30d, 90d, 365d,
    ending today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsBreakdownRange | Unset): Preset window ending today. Ignored when from
            or to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsBreakdownPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        by (GetAnalyticsBreakdownBy): The dimension to group by: platform, keyword, sentiment
            (unclassified included), intent (a mention can carry several), status (open, ignored,
            done), hour (weekday and hour of day in `timezone`), person (who posted; anonymous posts
            are left out).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsBreakdown | ErrorResponse
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
        by=by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsBreakdownRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsBreakdownPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    by: GetAnalyticsBreakdownBy,
) -> Response[AnalyticsBreakdown | ErrorResponse]:
    """Mentions grouped by one dimension

     One table of matched, relevant and sentiment counts grouped by `by`: platform, keyword, sentiment,
    intent, status, hour (weekday and hour of day) or person. The window is `range` (7d, 30d, 90d, 365d,
    ending today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsBreakdownRange | Unset): Preset window ending today. Ignored when from
            or to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsBreakdownPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        by (GetAnalyticsBreakdownBy): The dimension to group by: platform, keyword, sentiment
            (unclassified included), intent (a mention can carry several), status (open, ignored,
            done), hour (weekday and hour of day in `timezone`), person (who posted; anonymous posts
            are left out).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsBreakdown | ErrorResponse]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
        by=by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    range_: GetAnalyticsBreakdownRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetAnalyticsBreakdownPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    by: GetAnalyticsBreakdownBy,
) -> AnalyticsBreakdown | ErrorResponse | None:
    """Mentions grouped by one dimension

     One table of matched, relevant and sentiment counts grouped by `by`: platform, keyword, sentiment,
    intent, status, hour (weekday and hour of day) or person. The window is `range` (7d, 30d, 90d, 365d,
    ending today) or `from` and `to`, cut into days in `timezone` (UTC by default); `keywordIds` and
    `platforms` narrow it; `compare=true` adds the period of the same length right before it. Time axis
    is the publish date.

    Args:
        range_ (GetAnalyticsBreakdownRange | Unset): Preset window ending today. Ignored when from
            or to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetAnalyticsBreakdownPlatformsItem] | Unset): Only these platforms.
            Repeatable, or comma-separated; omit for every platform.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        by (GetAnalyticsBreakdownBy): The dimension to group by: platform, keyword, sentiment
            (unclassified included), intent (a mention can carry several), status (open, ignored,
            done), hour (weekday and hour of day in `timezone`), person (who posted; anonymous posts
            are left out).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsBreakdown | ErrorResponse
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
            by=by,
        )
    ).parsed
