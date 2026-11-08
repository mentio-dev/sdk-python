from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_reviews_report_bucket import GetReviewsReportBucket
from ...models.get_reviews_report_not_platforms_item import (
    GetReviewsReportNotPlatformsItem,
)
from ...models.get_reviews_report_platforms_item import GetReviewsReportPlatformsItem
from ...models.get_reviews_report_range import GetReviewsReportRange
from ...models.reviews_report import ReviewsReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    range_: GetReviewsReportRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetReviewsReportPlatformsItem] | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    not_platforms: list[GetReviewsReportNotPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetReviewsReportBucket | Unset = UNSET,
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

    json_not_keyword_ids: list[str] | None | Unset
    if isinstance(not_keyword_ids, Unset):
        json_not_keyword_ids = UNSET
    elif isinstance(not_keyword_ids, list):
        json_not_keyword_ids = not_keyword_ids

    else:
        json_not_keyword_ids = not_keyword_ids
    params["notKeywordIds"] = json_not_keyword_ids

    json_not_platforms: list[str] | Unset = UNSET
    if not isinstance(not_platforms, Unset):
        json_not_platforms = []
        for not_platforms_item_data in not_platforms:
            not_platforms_item = not_platforms_item_data.value
            json_not_platforms.append(not_platforms_item)

    params["notPlatforms"] = json_not_platforms

    params["compare"] = compare

    params["timezone"] = timezone

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket.value

    params["bucket"] = json_bucket

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/reviews",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ReviewsReport | None:
    if response.status_code == 200:
        response_200 = ReviewsReport.from_dict(response.json())

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
) -> Response[ErrorResponse | ReviewsReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetReviewsReportRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetReviewsReportPlatformsItem] | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    not_platforms: list[GetReviewsReportNotPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetReviewsReportBucket | Unset = UNSET,
) -> Response[ErrorResponse | ReviewsReport]:
    """Reviews: stars over a window, per review page

     Report on your keywords' reviews: count, average stars, distribution, replies and open 1-2 star
    reviews.

    Per page too, with unhappy reviews' tags; each review counts once.

    The window is `range` or `from` and `to`, in `timezone`, by publish date; `compare=true` adds the
    period before.

    Args:
        range_ (GetReviewsReportRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetReviewsReportPlatformsItem] | Unset): Only these platforms. Repeatable,
            or comma-separated; omit for every platform.
        not_keyword_ids (list[str] | None | Unset): Never these keyword ids. Repeatable, or comma-
            separated.
        not_platforms (list[GetReviewsReportNotPlatformsItem] | Unset): Never these platforms.
            Repeatable, or comma-separated.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetReviewsReportBucket | Unset): Series bucket: day (default up to 90 days) or
            week.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReviewsReport]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        not_keyword_ids=not_keyword_ids,
        not_platforms=not_platforms,
        compare=compare,
        timezone=timezone,
        bucket=bucket,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    range_: GetReviewsReportRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetReviewsReportPlatformsItem] | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    not_platforms: list[GetReviewsReportNotPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetReviewsReportBucket | Unset = UNSET,
) -> ErrorResponse | ReviewsReport | None:
    """Reviews: stars over a window, per review page

     Report on your keywords' reviews: count, average stars, distribution, replies and open 1-2 star
    reviews.

    Per page too, with unhappy reviews' tags; each review counts once.

    The window is `range` or `from` and `to`, in `timezone`, by publish date; `compare=true` adds the
    period before.

    Args:
        range_ (GetReviewsReportRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetReviewsReportPlatformsItem] | Unset): Only these platforms. Repeatable,
            or comma-separated; omit for every platform.
        not_keyword_ids (list[str] | None | Unset): Never these keyword ids. Repeatable, or comma-
            separated.
        not_platforms (list[GetReviewsReportNotPlatformsItem] | Unset): Never these platforms.
            Repeatable, or comma-separated.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetReviewsReportBucket | Unset): Series bucket: day (default up to 90 days) or
            week.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReviewsReport
    """

    return sync_detailed(
        client=client,
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        not_keyword_ids=not_keyword_ids,
        not_platforms=not_platforms,
        compare=compare,
        timezone=timezone,
        bucket=bucket,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetReviewsReportRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetReviewsReportPlatformsItem] | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    not_platforms: list[GetReviewsReportNotPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetReviewsReportBucket | Unset = UNSET,
) -> Response[ErrorResponse | ReviewsReport]:
    """Reviews: stars over a window, per review page

     Report on your keywords' reviews: count, average stars, distribution, replies and open 1-2 star
    reviews.

    Per page too, with unhappy reviews' tags; each review counts once.

    The window is `range` or `from` and `to`, in `timezone`, by publish date; `compare=true` adds the
    period before.

    Args:
        range_ (GetReviewsReportRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetReviewsReportPlatformsItem] | Unset): Only these platforms. Repeatable,
            or comma-separated; omit for every platform.
        not_keyword_ids (list[str] | None | Unset): Never these keyword ids. Repeatable, or comma-
            separated.
        not_platforms (list[GetReviewsReportNotPlatformsItem] | Unset): Never these platforms.
            Repeatable, or comma-separated.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetReviewsReportBucket | Unset): Series bucket: day (default up to 90 days) or
            week.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReviewsReport]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        not_keyword_ids=not_keyword_ids,
        not_platforms=not_platforms,
        compare=compare,
        timezone=timezone,
        bucket=bucket,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    range_: GetReviewsReportRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetReviewsReportPlatformsItem] | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    not_platforms: list[GetReviewsReportNotPlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    bucket: GetReviewsReportBucket | Unset = UNSET,
) -> ErrorResponse | ReviewsReport | None:
    """Reviews: stars over a window, per review page

     Report on your keywords' reviews: count, average stars, distribution, replies and open 1-2 star
    reviews.

    Per page too, with unhappy reviews' tags; each review counts once.

    The window is `range` or `from` and `to`, in `timezone`, by publish date; `compare=true` adds the
    period before.

    Args:
        range_ (GetReviewsReportRange | Unset): Preset window ending today. Ignored when from or
            to is given. Default 30d.
        from_ (str | Unset): First day, YYYY-MM-DD, inclusive, in `timezone`.
        to (str | Unset): Last day, YYYY-MM-DD, inclusive, in `timezone`. Default today.
        keyword_ids (list[str] | None | Unset): Only these keyword ids. Repeatable, or comma-
            separated; omit for every keyword.
        platforms (list[GetReviewsReportPlatformsItem] | Unset): Only these platforms. Repeatable,
            or comma-separated; omit for every platform.
        not_keyword_ids (list[str] | None | Unset): Never these keyword ids. Repeatable, or comma-
            separated.
        not_platforms (list[GetReviewsReportNotPlatformsItem] | Unset): Never these platforms.
            Repeatable, or comma-separated.
        compare (bool | Unset): true adds the period of the same length right before the window as
            `previous`.
        timezone (str | Unset): IANA zone the days are cut in (Europe/Madrid). Default UTC. One
            offset, the zone's at the end of the window, applies to the whole window.
        bucket (GetReviewsReportBucket | Unset): Series bucket: day (default up to 90 days) or
            week.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReviewsReport
    """

    return (
        await asyncio_detailed(
            client=client,
            range_=range_,
            from_=from_,
            to=to,
            keyword_ids=keyword_ids,
            platforms=platforms,
            not_keyword_ids=not_keyword_ids,
            not_platforms=not_platforms,
            compare=compare,
            timezone=timezone,
            bucket=bucket,
        )
    ).parsed
