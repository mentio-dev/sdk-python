from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.tracked_account import TrackedAccount
from ...models.update_account_body import UpdateAccountBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateAccountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/accounts/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TrackedAccount | None:
    if response.status_code == 200:
        response_200 = TrackedAccount.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | TrackedAccount]:
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
    body: UpdateAccountBody,
) -> Response[ErrorResponse | TrackedAccount]:
    """Update a tracked account

     Pause, resume, move or cap a tracked account.

    - `muted`: a paused account is neither read nor charged.
    - `groupId`: move it to another keyword group.
    - `cap`: the monthly follower cap; null removes it, a raise resumes it.

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        body (UpdateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TrackedAccount]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAccountBody,
) -> ErrorResponse | TrackedAccount | None:
    """Update a tracked account

     Pause, resume, move or cap a tracked account.

    - `muted`: a paused account is neither read nor charged.
    - `groupId`: move it to another keyword group.
    - `cap`: the monthly follower cap; null removes it, a raise resumes it.

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        body (UpdateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TrackedAccount
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAccountBody,
) -> Response[ErrorResponse | TrackedAccount]:
    """Update a tracked account

     Pause, resume, move or cap a tracked account.

    - `muted`: a paused account is neither read nor charged.
    - `groupId`: move it to another keyword group.
    - `cap`: the monthly follower cap; null removes it, a raise resumes it.

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        body (UpdateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TrackedAccount]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAccountBody,
) -> ErrorResponse | TrackedAccount | None:
    """Update a tracked account

     Pause, resume, move or cap a tracked account.

    - `muted`: a paused account is neither read nor charged.
    - `groupId`: move it to another keyword group.
    - `cap`: the monthly follower cap; null removes it, a raise resumes it.

    Args:
        id (str): Tracked account id (acc_...). Example: acc_abc123.
        body (UpdateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TrackedAccount
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
