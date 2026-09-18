from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_invitation_body import CreateInvitationBody
from ...models.error_response import ErrorResponse
from ...models.invitation import Invitation
from ...types import Response


def _get_kwargs(
    *,
    body: CreateInvitationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/members/invitations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Invitation | None:
    if response.status_code == 200:
        response_200 = Invitation.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Invitation.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Invitation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInvitationBody,
) -> Response[ErrorResponse | Invitation]:
    """Invite a member

     Send an email invitation to join the workspace as admin or member; it expires after 48 hours.
    Idempotent: an address that already holds an open invitation gets it back with 200 and no second
    email. An address that is already a member is a 409 already_member. Team changes need a signed-in
    owner or admin (an OAuth token from an MCP sign-in, or the dashboard session): an API key answers
    403.

    Args:
        body (CreateInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Invitation]
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
    body: CreateInvitationBody,
) -> ErrorResponse | Invitation | None:
    """Invite a member

     Send an email invitation to join the workspace as admin or member; it expires after 48 hours.
    Idempotent: an address that already holds an open invitation gets it back with 200 and no second
    email. An address that is already a member is a 409 already_member. Team changes need a signed-in
    owner or admin (an OAuth token from an MCP sign-in, or the dashboard session): an API key answers
    403.

    Args:
        body (CreateInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Invitation
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInvitationBody,
) -> Response[ErrorResponse | Invitation]:
    """Invite a member

     Send an email invitation to join the workspace as admin or member; it expires after 48 hours.
    Idempotent: an address that already holds an open invitation gets it back with 200 and no second
    email. An address that is already a member is a 409 already_member. Team changes need a signed-in
    owner or admin (an OAuth token from an MCP sign-in, or the dashboard session): an API key answers
    403.

    Args:
        body (CreateInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Invitation]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateInvitationBody,
) -> ErrorResponse | Invitation | None:
    """Invite a member

     Send an email invitation to join the workspace as admin or member; it expires after 48 hours.
    Idempotent: an address that already holds an open invitation gets it back with 200 and no second
    email. An address that is already a member is a 409 already_member. Team changes need a signed-in
    owner or admin (an OAuth token from an MCP sign-in, or the dashboard session): an API key answers
    403.

    Args:
        body (CreateInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Invitation
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
