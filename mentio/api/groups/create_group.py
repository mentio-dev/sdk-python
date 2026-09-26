from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_group_body import CreateGroupBody
from ...models.error_response import ErrorResponse
from ...models.group import Group
from ...types import Response


def _get_kwargs(
    *,
    body: CreateGroupBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/groups",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Group | None:
    if response.status_code == 201:
        response_201 = Group.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Group]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateGroupBody,
) -> Response[ErrorResponse | Group]:
    """Create a group

     Create a keyword group. `name` is unique per workspace; `externalId` (optional, unique too) is your
    own id for it, a customer id say, so you can find it again without storing ours; `context`
    (optional) is the group's own company description, which the classifier reads in place of the whole
    workspace profile for the group's keywords. Then pass the group id as `groupId` when creating a
    keyword.

    Args:
        body (CreateGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Group]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateGroupBody,
) -> ErrorResponse | Group | None:
    """Create a group

     Create a keyword group. `name` is unique per workspace; `externalId` (optional, unique too) is your
    own id for it, a customer id say, so you can find it again without storing ours; `context`
    (optional) is the group's own company description, which the classifier reads in place of the whole
    workspace profile for the group's keywords. Then pass the group id as `groupId` when creating a
    keyword.

    Args:
        body (CreateGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Group
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateGroupBody,
) -> Response[ErrorResponse | Group]:
    """Create a group

     Create a keyword group. `name` is unique per workspace; `externalId` (optional, unique too) is your
    own id for it, a customer id say, so you can find it again without storing ours; `context`
    (optional) is the group's own company description, which the classifier reads in place of the whole
    workspace profile for the group's keywords. Then pass the group id as `groupId` when creating a
    keyword.

    Args:
        body (CreateGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Group]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateGroupBody,
) -> ErrorResponse | Group | None:
    """Create a group

     Create a keyword group. `name` is unique per workspace; `externalId` (optional, unique too) is your
    own id for it, a customer id say, so you can find it again without storing ours; `context`
    (optional) is the group's own company description, which the classifier reads in place of the whole
    workspace profile for the group's keywords. Then pass the group id as `groupId` when creating a
    keyword.

    Args:
        body (CreateGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Group
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
