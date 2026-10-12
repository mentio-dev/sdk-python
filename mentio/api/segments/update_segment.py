from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.segment import Segment
from ...models.update_segment_body import UpdateSegmentBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: UpdateSegmentBody,
    group_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/segments/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Segment | None:
    if response.status_code == 200:
        response_200 = Segment.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

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
) -> Response[ErrorResponse | Segment]:
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
    body: UpdateSegmentBody,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | Segment]:
    """Update a segment

     Only the fields sent change. Pass the `groupId` the segment was saved in; a segment cannot move
    between scopes.

    Args:
        id (str): Segment id (seg_...). Example: seg_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (UpdateSegmentBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Segment]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSegmentBody,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | Segment | None:
    """Update a segment

     Only the fields sent change. Pass the `groupId` the segment was saved in; a segment cannot move
    between scopes.

    Args:
        id (str): Segment id (seg_...). Example: seg_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (UpdateSegmentBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Segment
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSegmentBody,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | Segment]:
    """Update a segment

     Only the fields sent change. Pass the `groupId` the segment was saved in; a segment cannot move
    between scopes.

    Args:
        id (str): Segment id (seg_...). Example: seg_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (UpdateSegmentBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Segment]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSegmentBody,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | Segment | None:
    """Update a segment

     Only the fields sent change. Pass the `groupId` the segment was saved in; a segment cannot move
    between scopes.

    Args:
        id (str): Segment id (seg_...). Example: seg_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (UpdateSegmentBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Segment
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            group_id=group_id,
        )
    ).parsed
