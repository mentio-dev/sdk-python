from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    workspace_ids: list[str] | None | Unset = UNSET,
    not_workspace_ids: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_workspace_ids: list[str] | None | Unset
    if isinstance(workspace_ids, Unset):
        json_workspace_ids = UNSET
    elif isinstance(workspace_ids, list):
        json_workspace_ids = workspace_ids

    else:
        json_workspace_ids = workspace_ids
    params["workspaceIds"] = json_workspace_ids

    json_not_workspace_ids: list[str] | None | Unset
    if isinstance(not_workspace_ids, Unset):
        json_not_workspace_ids = UNSET
    elif isinstance(not_workspace_ids, list):
        json_not_workspace_ids = not_workspace_ids

    else:
        json_not_workspace_ids = not_workspace_ids
    params["notWorkspaceIds"] = json_not_workspace_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/workspace-members/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ErrorResponse]:
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
    workspace_ids: list[str] | None | Unset = UNSET,
    not_workspace_ids: list[str] | None | Unset = UNSET,
) -> Response[Any | ErrorResponse]:
    """Remove someone from your child workspaces

     Removes the person from every child workspace, or from the ones `workspaceIds` names, or from all
    but `notWorkspaceIds`. Never from your own workspace (that is DELETE /v1/members/{id}). Needs a
    signed-in owner or admin, not an API key.

    Args:
        id (str): The person's user id, from GET /v1/workspace-members. Example: usr_abc123.
        workspace_ids (list[str] | None | Unset): Only from these child workspaces (org_...);
            default every child. Never the parent: its own team is managed on /v1/members. Repeatable,
            or comma-separated.
        not_workspace_ids (list[str] | None | Unset): From every child workspace except these
            (org_...). Repeatable, or comma-separated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        workspace_ids=workspace_ids,
        not_workspace_ids=not_workspace_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    workspace_ids: list[str] | None | Unset = UNSET,
    not_workspace_ids: list[str] | None | Unset = UNSET,
) -> Any | ErrorResponse | None:
    """Remove someone from your child workspaces

     Removes the person from every child workspace, or from the ones `workspaceIds` names, or from all
    but `notWorkspaceIds`. Never from your own workspace (that is DELETE /v1/members/{id}). Needs a
    signed-in owner or admin, not an API key.

    Args:
        id (str): The person's user id, from GET /v1/workspace-members. Example: usr_abc123.
        workspace_ids (list[str] | None | Unset): Only from these child workspaces (org_...);
            default every child. Never the parent: its own team is managed on /v1/members. Repeatable,
            or comma-separated.
        not_workspace_ids (list[str] | None | Unset): From every child workspace except these
            (org_...). Repeatable, or comma-separated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        workspace_ids=workspace_ids,
        not_workspace_ids=not_workspace_ids,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    workspace_ids: list[str] | None | Unset = UNSET,
    not_workspace_ids: list[str] | None | Unset = UNSET,
) -> Response[Any | ErrorResponse]:
    """Remove someone from your child workspaces

     Removes the person from every child workspace, or from the ones `workspaceIds` names, or from all
    but `notWorkspaceIds`. Never from your own workspace (that is DELETE /v1/members/{id}). Needs a
    signed-in owner or admin, not an API key.

    Args:
        id (str): The person's user id, from GET /v1/workspace-members. Example: usr_abc123.
        workspace_ids (list[str] | None | Unset): Only from these child workspaces (org_...);
            default every child. Never the parent: its own team is managed on /v1/members. Repeatable,
            or comma-separated.
        not_workspace_ids (list[str] | None | Unset): From every child workspace except these
            (org_...). Repeatable, or comma-separated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        workspace_ids=workspace_ids,
        not_workspace_ids=not_workspace_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    workspace_ids: list[str] | None | Unset = UNSET,
    not_workspace_ids: list[str] | None | Unset = UNSET,
) -> Any | ErrorResponse | None:
    """Remove someone from your child workspaces

     Removes the person from every child workspace, or from the ones `workspaceIds` names, or from all
    but `notWorkspaceIds`. Never from your own workspace (that is DELETE /v1/members/{id}). Needs a
    signed-in owner or admin, not an API key.

    Args:
        id (str): The person's user id, from GET /v1/workspace-members. Example: usr_abc123.
        workspace_ids (list[str] | None | Unset): Only from these child workspaces (org_...);
            default every child. Never the parent: its own team is managed on /v1/members. Repeatable,
            or comma-separated.
        not_workspace_ids (list[str] | None | Unset): From every child workspace except these
            (org_...). Repeatable, or comma-separated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            workspace_ids=workspace_ids,
            not_workspace_ids=not_workspace_ids,
        )
    ).parsed
