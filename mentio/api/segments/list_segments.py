from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_segments_response_200 import ListSegmentsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/segments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListSegmentsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListSegmentsResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | ListSegmentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | ListSegmentsResponse200]:
    """List segments

     Your saved segments, each with the number of people in it right now (segments are evaluated on every
    read, never materialized), plus presets you can save as a starting point. Pass a segment id to GET
    /v1/people to list its members. With `groupId`, that keyword group's own segments, counted over its
    own people; without it, the workspace's. A segment belongs to one scope and is not visible from
    another.

    Args:
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListSegmentsResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | ListSegmentsResponse200 | None:
    """List segments

     Your saved segments, each with the number of people in it right now (segments are evaluated on every
    read, never materialized), plus presets you can save as a starting point. Pass a segment id to GET
    /v1/people to list its members. With `groupId`, that keyword group's own segments, counted over its
    own people; without it, the workspace's. A segment belongs to one scope and is not visible from
    another.

    Args:
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListSegmentsResponse200
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | ListSegmentsResponse200]:
    """List segments

     Your saved segments, each with the number of people in it right now (segments are evaluated on every
    read, never materialized), plus presets you can save as a starting point. Pass a segment id to GET
    /v1/people to list its members. With `groupId`, that keyword group's own segments, counted over its
    own people; without it, the workspace's. A segment belongs to one scope and is not visible from
    another.

    Args:
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListSegmentsResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | ListSegmentsResponse200 | None:
    """List segments

     Your saved segments, each with the number of people in it right now (segments are evaluated on every
    read, never materialized), plus presets you can save as a starting point. Pass a segment id to GET
    /v1/people to list its members. With `groupId`, that keyword group's own segments, counted over its
    own people; without it, the workspace's. A segment belongs to one scope and is not visible from
    another.

    Args:
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListSegmentsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
        )
    ).parsed
