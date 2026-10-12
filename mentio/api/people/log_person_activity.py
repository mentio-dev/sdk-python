from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.log_person_activity_body import LogPersonActivityBody
from ...models.person_activity import PersonActivity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: LogPersonActivityBody,
    group_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/people/{id}/activities".format(
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
) -> ErrorResponse | PersonActivity | None:
    if response.status_code == 201:
        response_201 = PersonActivity.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | PersonActivity]:
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
    body: LogPersonActivityBody,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | PersonActivity]:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call. The first activity claims
    an unowned person for whoever reached out and moves not_contacted to contacted; an existing owner
    and a later stage are kept. `memberId` defaults to the signed-in member; an API key that omits it
    logs an unattributed activity, which claims nobody. With `groupId`, the call works inside that
    keyword group: its people, and its own tags, notes, mute, merges and activities, apart from the
    workspace's and from every other group's.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (LogPersonActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PersonActivity]
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
    body: LogPersonActivityBody,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | PersonActivity | None:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call. The first activity claims
    an unowned person for whoever reached out and moves not_contacted to contacted; an existing owner
    and a later stage are kept. `memberId` defaults to the signed-in member; an API key that omits it
    logs an unattributed activity, which claims nobody. With `groupId`, the call works inside that
    keyword group: its people, and its own tags, notes, mute, merges and activities, apart from the
    workspace's and from every other group's.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (LogPersonActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PersonActivity
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
    body: LogPersonActivityBody,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | PersonActivity]:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call. The first activity claims
    an unowned person for whoever reached out and moves not_contacted to contacted; an existing owner
    and a later stage are kept. `memberId` defaults to the signed-in member; an API key that omits it
    logs an unattributed activity, which claims nobody. With `groupId`, the call works inside that
    keyword group: its people, and its own tags, notes, mute, merges and activities, apart from the
    workspace's and from every other group's.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (LogPersonActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PersonActivity]
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
    body: LogPersonActivityBody,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | PersonActivity | None:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call. The first activity claims
    an unowned person for whoever reached out and moves not_contacted to contacted; an existing owner
    and a later stage are kept. `memberId` defaults to the signed-in member; an API key that omits it
    logs an unattributed activity, which claims nobody. With `groupId`, the call works inside that
    keyword group: its people, and its own tags, notes, mute, merges and activities, apart from the
    workspace's and from every other group's.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        body (LogPersonActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PersonActivity
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            group_id=group_id,
        )
    ).parsed
