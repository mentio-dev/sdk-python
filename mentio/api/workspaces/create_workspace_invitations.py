from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_workspace_invitations_body import CreateWorkspaceInvitationsBody
from ...models.create_workspace_invitations_response_201 import (
    CreateWorkspaceInvitationsResponse201,
)
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateWorkspaceInvitationsBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workspace-invitations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateWorkspaceInvitationsResponse201 | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = CreateWorkspaceInvitationsResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateWorkspaceInvitationsResponse201 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWorkspaceInvitationsBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateWorkspaceInvitationsResponse201 | ErrorResponse]:
    """Invite someone to several child workspaces

     Invites one address to several child workspaces, one email each. A member or an open invitation is
    reported, never sent twice. Needs a signed-in owner or admin, not an API key.

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateWorkspaceInvitationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkspaceInvitationsResponse201 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateWorkspaceInvitationsBody,
    idempotency_key: str | Unset = UNSET,
) -> CreateWorkspaceInvitationsResponse201 | ErrorResponse | None:
    """Invite someone to several child workspaces

     Invites one address to several child workspaces, one email each. A member or an open invitation is
    reported, never sent twice. Needs a signed-in owner or admin, not an API key.

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateWorkspaceInvitationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkspaceInvitationsResponse201 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWorkspaceInvitationsBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateWorkspaceInvitationsResponse201 | ErrorResponse]:
    """Invite someone to several child workspaces

     Invites one address to several child workspaces, one email each. A member or an open invitation is
    reported, never sent twice. Needs a signed-in owner or admin, not an API key.

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateWorkspaceInvitationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkspaceInvitationsResponse201 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateWorkspaceInvitationsBody,
    idempotency_key: str | Unset = UNSET,
) -> CreateWorkspaceInvitationsResponse201 | ErrorResponse | None:
    """Invite someone to several child workspaces

     Invites one address to several child workspaces, one email each. A member or an open invitation is
    reported, never sent twice. Needs a signed-in owner or admin, not an API key.

    Args:
        idempotency_key (str | Unset): A unique value (a UUID) for this request. Retrying with the
            same key within 24 hours returns the first response instead of creating twice. Example:
            7b1e4c2a-9f3d-4e8a-b6c5-1d2e3f4a5b6c.
        body (CreateWorkspaceInvitationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkspaceInvitationsResponse201 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
