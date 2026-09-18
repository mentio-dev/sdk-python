from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.mention import Mention
from ...models.update_mention_body import UpdateMentionBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateMentionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/mentions/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Mention | None:
    if response.status_code == 200:
        response_200 = Mention.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Mention]:
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
    body: UpdateMentionBody,
) -> Response[ErrorResponse | Mention]:
    """Update a mention

     The one write on a mention. Set status to ignored or done to handle it (open puts it back), assign
    it to a workspace member, snooze it out of the feed, leave an internal note, or correct the
    classifier: `relevant` true or false is your verdict (relevance becomes 100 or 0, and every list,
    filter, digest and report follows it), `sentiment` replaces the label; null withdraws a verdict and
    restores the classifier's value. Omitted fields are untouched. Delivery and billing never change.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        body (UpdateMentionBody): Every field is optional; omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Mention]
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
    body: UpdateMentionBody,
) -> ErrorResponse | Mention | None:
    """Update a mention

     The one write on a mention. Set status to ignored or done to handle it (open puts it back), assign
    it to a workspace member, snooze it out of the feed, leave an internal note, or correct the
    classifier: `relevant` true or false is your verdict (relevance becomes 100 or 0, and every list,
    filter, digest and report follows it), `sentiment` replaces the label; null withdraws a verdict and
    restores the classifier's value. Omitted fields are untouched. Delivery and billing never change.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        body (UpdateMentionBody): Every field is optional; omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Mention
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
    body: UpdateMentionBody,
) -> Response[ErrorResponse | Mention]:
    """Update a mention

     The one write on a mention. Set status to ignored or done to handle it (open puts it back), assign
    it to a workspace member, snooze it out of the feed, leave an internal note, or correct the
    classifier: `relevant` true or false is your verdict (relevance becomes 100 or 0, and every list,
    filter, digest and report follows it), `sentiment` replaces the label; null withdraws a verdict and
    restores the classifier's value. Omitted fields are untouched. Delivery and billing never change.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        body (UpdateMentionBody): Every field is optional; omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Mention]
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
    body: UpdateMentionBody,
) -> ErrorResponse | Mention | None:
    """Update a mention

     The one write on a mention. Set status to ignored or done to handle it (open puts it back), assign
    it to a workspace member, snooze it out of the feed, leave an internal note, or correct the
    classifier: `relevant` true or false is your verdict (relevance becomes 100 or 0, and every list,
    filter, digest and report follows it), `sentiment` replaces the label; null withdraws a verdict and
    restores the classifier's value. Omitted fields are untouched. Delivery and billing never change.

    Args:
        id (str): Mention id (mm_...). Example: mm_abc123.
        body (UpdateMentionBody): Every field is optional; omitted fields are untouched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Mention
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
