from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_account_followers_range import ListAccountFollowersRange
from ...models.list_account_followers_response_200 import (
    ListAccountFollowersResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    range_: ListAccountFollowersRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    include_baseline: bool | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["from"] = from_

    params["to"] = to

    params["timezone"] = timezone

    params["includeBaseline"] = include_baseline

    json_min_followers: int | None | Unset
    if isinstance(min_followers, Unset):
        json_min_followers = UNSET
    else:
        json_min_followers = min_followers
    params["minFollowers"] = json_min_followers

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/accounts/{id}/followers".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListAccountFollowersResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAccountFollowersResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | ListAccountFollowersResponse200]:
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
    range_: ListAccountFollowersRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    include_baseline: bool | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | ListAccountFollowersResponse200]:
    """List an account's followers

     A tracked account's new followers, newest first, cursor paged.

    `includeBaseline=true` adds the ones the first read found. Filter by when they were first seen
    (`range`, `from`, `to`), their reach (`minFollowers`) or text (`q`).

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        range_ (ListAccountFollowersRange | Unset): A preset window ending now: 7d is today and
            the six days before, in `timezone`, as in the analytics reports. Ignored when from or to
            is given. Omit range, from and to for no window.
        from_ (str | Unset): Start, inclusive: a day (YYYY-MM-DD, from its first moment in
            `timezone`) or an instant (ISO 8601 with its offset, or epoch ms).
        to (str | Unset): End, inclusive: a day (YYYY-MM-DD, to its last moment in `timezone`) or
            an instant (ISO 8601 with its offset, or epoch ms).
        timezone (str | Unset): IANA zone that days in range, from and to are cut in
            (Europe/Madrid). Default UTC.
        include_baseline (bool | Unset): true: also the followers the first read found. Default
            false: only new ones.
        min_followers (int | None | Unset): Only followers with at least this many followers of
            their own.
        q (str | Unset): Text in the handle, the name or the bio.
        limit (int | Unset): Page size, 1 to 100. Default 50. Default: 50.
        cursor (str | Unset): From the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAccountFollowersResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        from_=from_,
        to=to,
        timezone=timezone,
        include_baseline=include_baseline,
        min_followers=min_followers,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: ListAccountFollowersRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    include_baseline: bool | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | ListAccountFollowersResponse200 | None:
    """List an account's followers

     A tracked account's new followers, newest first, cursor paged.

    `includeBaseline=true` adds the ones the first read found. Filter by when they were first seen
    (`range`, `from`, `to`), their reach (`minFollowers`) or text (`q`).

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        range_ (ListAccountFollowersRange | Unset): A preset window ending now: 7d is today and
            the six days before, in `timezone`, as in the analytics reports. Ignored when from or to
            is given. Omit range, from and to for no window.
        from_ (str | Unset): Start, inclusive: a day (YYYY-MM-DD, from its first moment in
            `timezone`) or an instant (ISO 8601 with its offset, or epoch ms).
        to (str | Unset): End, inclusive: a day (YYYY-MM-DD, to its last moment in `timezone`) or
            an instant (ISO 8601 with its offset, or epoch ms).
        timezone (str | Unset): IANA zone that days in range, from and to are cut in
            (Europe/Madrid). Default UTC.
        include_baseline (bool | Unset): true: also the followers the first read found. Default
            false: only new ones.
        min_followers (int | None | Unset): Only followers with at least this many followers of
            their own.
        q (str | Unset): Text in the handle, the name or the bio.
        limit (int | Unset): Page size, 1 to 100. Default 50. Default: 50.
        cursor (str | Unset): From the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAccountFollowersResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        range_=range_,
        from_=from_,
        to=to,
        timezone=timezone,
        include_baseline=include_baseline,
        min_followers=min_followers,
        q=q,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: ListAccountFollowersRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    include_baseline: bool | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | ListAccountFollowersResponse200]:
    """List an account's followers

     A tracked account's new followers, newest first, cursor paged.

    `includeBaseline=true` adds the ones the first read found. Filter by when they were first seen
    (`range`, `from`, `to`), their reach (`minFollowers`) or text (`q`).

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        range_ (ListAccountFollowersRange | Unset): A preset window ending now: 7d is today and
            the six days before, in `timezone`, as in the analytics reports. Ignored when from or to
            is given. Omit range, from and to for no window.
        from_ (str | Unset): Start, inclusive: a day (YYYY-MM-DD, from its first moment in
            `timezone`) or an instant (ISO 8601 with its offset, or epoch ms).
        to (str | Unset): End, inclusive: a day (YYYY-MM-DD, to its last moment in `timezone`) or
            an instant (ISO 8601 with its offset, or epoch ms).
        timezone (str | Unset): IANA zone that days in range, from and to are cut in
            (Europe/Madrid). Default UTC.
        include_baseline (bool | Unset): true: also the followers the first read found. Default
            false: only new ones.
        min_followers (int | None | Unset): Only followers with at least this many followers of
            their own.
        q (str | Unset): Text in the handle, the name or the bio.
        limit (int | Unset): Page size, 1 to 100. Default 50. Default: 50.
        cursor (str | Unset): From the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAccountFollowersResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        from_=from_,
        to=to,
        timezone=timezone,
        include_baseline=include_baseline,
        min_followers=min_followers,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: ListAccountFollowersRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
    include_baseline: bool | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | ListAccountFollowersResponse200 | None:
    """List an account's followers

     A tracked account's new followers, newest first, cursor paged.

    `includeBaseline=true` adds the ones the first read found. Filter by when they were first seen
    (`range`, `from`, `to`), their reach (`minFollowers`) or text (`q`).

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        range_ (ListAccountFollowersRange | Unset): A preset window ending now: 7d is today and
            the six days before, in `timezone`, as in the analytics reports. Ignored when from or to
            is given. Omit range, from and to for no window.
        from_ (str | Unset): Start, inclusive: a day (YYYY-MM-DD, from its first moment in
            `timezone`) or an instant (ISO 8601 with its offset, or epoch ms).
        to (str | Unset): End, inclusive: a day (YYYY-MM-DD, to its last moment in `timezone`) or
            an instant (ISO 8601 with its offset, or epoch ms).
        timezone (str | Unset): IANA zone that days in range, from and to are cut in
            (Europe/Madrid). Default UTC.
        include_baseline (bool | Unset): true: also the followers the first read found. Default
            false: only new ones.
        min_followers (int | None | Unset): Only followers with at least this many followers of
            their own.
        q (str | Unset): Text in the handle, the name or the bio.
        limit (int | Unset): Page size, 1 to 100. Default 50. Default: 50.
        cursor (str | Unset): From the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAccountFollowersResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            range_=range_,
            from_=from_,
            to=to,
            timezone=timezone,
            include_baseline=include_baseline,
            min_followers=min_followers,
            q=q,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
