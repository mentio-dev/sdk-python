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
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

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
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | PersonActivity]:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call.

    The first claims an unowned person and marks them contacted; without `memberId`, a key's activity
    claims nobody.

    With `groupId`, it acts inside that keyword group; see [Groups](/guides/groups#people-and-segments-
    by-group).

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
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
        idempotency_key=idempotency_key,
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
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | PersonActivity | None:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call.

    The first claims an unowned person and marks them contacted; without `memberId`, a key's activity
    claims nobody.

    With `groupId`, it acts inside that keyword group; see [Groups](/guides/groups#people-and-segments-
    by-group).

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
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
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: LogPersonActivityBody,
    group_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | PersonActivity]:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call.

    The first claims an unowned person and marks them contacted; without `memberId`, a key's activity
    claims nobody.

    With `groupId`, it acts inside that keyword group; see [Groups](/guides/groups#people-and-segments-
    by-group).

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
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
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: LogPersonActivityBody,
    group_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | PersonActivity | None:
    """Log an outreach activity

     Record that a teammate reached out to this person: an email, a DM, a call.

    The first claims an unowned person and marks them contacted; without `memberId`, a key's activity
    claims nobody.

    With `groupId`, it acts inside that keyword group; see [Groups](/guides/groups#people-and-segments-
    by-group).

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, mute, merges, activities and
            segments. Omit for the whole workspace.
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
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
            idempotency_key=idempotency_key,
        )
    ).parsed
