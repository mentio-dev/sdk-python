from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_groups_response_200 import ListGroupsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    external_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["externalId"] = external_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListGroupsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListGroupsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ListGroupsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    external_id: str | Unset = UNSET,
) -> Response[ErrorResponse | ListGroupsResponse200]:
    """List groups

     The keyword groups of the workspace, the default group first, then oldest first. A group is how
    keywords are grouped (a customer, a campaign, a product): a term may be tracked once per group,
    every keyword belongs to one, and GET /v1/usage/breakdown?by=group says what each group cost. Pass
    `externalId` to find the group carrying your own id.

    Args:
        external_id (str | Unset): Only the group carrying exactly this externalId.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListGroupsResponse200]
    """

    kwargs = _get_kwargs(
        external_id=external_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    external_id: str | Unset = UNSET,
) -> ErrorResponse | ListGroupsResponse200 | None:
    """List groups

     The keyword groups of the workspace, the default group first, then oldest first. A group is how
    keywords are grouped (a customer, a campaign, a product): a term may be tracked once per group,
    every keyword belongs to one, and GET /v1/usage/breakdown?by=group says what each group cost. Pass
    `externalId` to find the group carrying your own id.

    Args:
        external_id (str | Unset): Only the group carrying exactly this externalId.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListGroupsResponse200
    """

    return sync_detailed(
        client=client,
        external_id=external_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    external_id: str | Unset = UNSET,
) -> Response[ErrorResponse | ListGroupsResponse200]:
    """List groups

     The keyword groups of the workspace, the default group first, then oldest first. A group is how
    keywords are grouped (a customer, a campaign, a product): a term may be tracked once per group,
    every keyword belongs to one, and GET /v1/usage/breakdown?by=group says what each group cost. Pass
    `externalId` to find the group carrying your own id.

    Args:
        external_id (str | Unset): Only the group carrying exactly this externalId.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListGroupsResponse200]
    """

    kwargs = _get_kwargs(
        external_id=external_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    external_id: str | Unset = UNSET,
) -> ErrorResponse | ListGroupsResponse200 | None:
    """List groups

     The keyword groups of the workspace, the default group first, then oldest first. A group is how
    keywords are grouped (a customer, a campaign, a product): a term may be tracked once per group,
    every keyword belongs to one, and GET /v1/usage/breakdown?by=group says what each group cost. Pass
    `externalId` to find the group carrying your own id.

    Args:
        external_id (str | Unset): Only the group carrying exactly this externalId.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListGroupsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            external_id=external_id,
        )
    ).parsed
