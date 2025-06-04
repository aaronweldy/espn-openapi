from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entry_response import EntryResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    challenge_name: str,
    user_id: str,
    *,
    view: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["view"] = view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v1/challenges/{challenge_name}/entries/{user_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EntryResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = EntryResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[EntryResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    challenge_name: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, str] = UNSET,
) -> Response[Union[EntryResponse, ErrorResponse]]:
    """Get User Entry

     Retrieve a specific user's entry in a challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        user_id (str):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntryResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        challenge_name=challenge_name,
        user_id=user_id,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    challenge_name: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, str] = UNSET,
) -> Optional[Union[EntryResponse, ErrorResponse]]:
    """Get User Entry

     Retrieve a specific user's entry in a challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        user_id (str):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntryResponse, ErrorResponse]
    """

    return sync_detailed(
        challenge_name=challenge_name,
        user_id=user_id,
        client=client,
        view=view,
    ).parsed


async def asyncio_detailed(
    challenge_name: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, str] = UNSET,
) -> Response[Union[EntryResponse, ErrorResponse]]:
    """Get User Entry

     Retrieve a specific user's entry in a challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        user_id (str):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntryResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        challenge_name=challenge_name,
        user_id=user_id,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    challenge_name: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, str] = UNSET,
) -> Optional[Union[EntryResponse, ErrorResponse]]:
    """Get User Entry

     Retrieve a specific user's entry in a challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        user_id (str):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntryResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            challenge_name=challenge_name,
            user_id=user_id,
            client=client,
            view=view,
        )
    ).parsed
