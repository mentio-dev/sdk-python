from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.person import Person
from ...models.update_person_body import UpdatePersonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: UpdatePersonBody,
    group_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/people/{id}".format(
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
) -> ErrorResponse | Person | None:
    if response.status_code == 200:
        response_200 = Person.from_dict(response.json())

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
) -> Response[ErrorResponse | Person]:
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
    body: UpdatePersonBody,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | Person]:
    """Update your annotations on a person

     Tags, notes, mute, and the outreach owner (a workspace member; null clears) and stage, for your
    workspace only. Mute hides their posts from your feed and every channel; ingest and billing never
    change. With `groupId` the annotations are that keyword group's own; `muted` is not supported there
    yet and is a 400.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, merges, activities and segments.
            Omit for the whole workspace.
        body (UpdatePersonBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Person]
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
    body: UpdatePersonBody,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | Person | None:
    """Update your annotations on a person

     Tags, notes, mute, and the outreach owner (a workspace member; null clears) and stage, for your
    workspace only. Mute hides their posts from your feed and every channel; ingest and billing never
    change. With `groupId` the annotations are that keyword group's own; `muted` is not supported there
    yet and is a 400.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, merges, activities and segments.
            Omit for the whole workspace.
        body (UpdatePersonBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Person
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
    body: UpdatePersonBody,
    group_id: str | Unset = UNSET,
) -> Response[ErrorResponse | Person]:
    """Update your annotations on a person

     Tags, notes, mute, and the outreach owner (a workspace member; null clears) and stage, for your
    workspace only. Mute hides their posts from your feed and every channel; ingest and billing never
    change. With `groupId` the annotations are that keyword group's own; `muted` is not supported there
    yet and is a 400.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, merges, activities and segments.
            Omit for the whole workspace.
        body (UpdatePersonBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Person]
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
    body: UpdatePersonBody,
    group_id: str | Unset = UNSET,
) -> ErrorResponse | Person | None:
    """Update your annotations on a person

     Tags, notes, mute, and the outreach owner (a workspace member; null clears) and stage, for your
    workspace only. Mute hides their posts from your feed and every channel; ingest and billing never
    change. With `groupId` the annotations are that keyword group's own; `muted` is not supported there
    yet and is a 400.

    Args:
        id (str): Person id (aut_...). Example: aut_abc123.
        group_id (str | Unset): Scope to one keyword group (grp_...): only people who mentioned
            that group's keywords, with that group's own tags, notes, merges, activities and segments.
            Omit for the whole workspace.
        body (UpdatePersonBody): Omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Person
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            group_id=group_id,
        )
    ).parsed
