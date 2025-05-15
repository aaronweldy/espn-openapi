from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.plays_list_response import PlaysListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    competition_id: str,
    *,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/football/leagues/nfl/events/{event_id}/competitions/{competition_id}/plays",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PlaysListResponse]]:
    if response.status_code == 200:
        response_200 = PlaysListResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PlaysListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PlaysListResponse]]:
    """Get Plays for a Competition

     Retrieve all plays for a given NFL event/competition.

    Args:
        event_id (str):
        competition_id (str):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PlaysListResponse]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        competition_id=competition_id,
        page_index=page_index,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PlaysListResponse]]:
    """Get Plays for a Competition

     Retrieve all plays for a given NFL event/competition.

    Args:
        event_id (str):
        competition_id (str):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PlaysListResponse]
    """

    return sync_detailed(
        event_id=event_id,
        competition_id=competition_id,
        client=client,
        page_index=page_index,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PlaysListResponse]]:
    """Get Plays for a Competition

     Retrieve all plays for a given NFL event/competition.

    Args:
        event_id (str):
        competition_id (str):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PlaysListResponse]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        competition_id=competition_id,
        page_index=page_index,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PlaysListResponse]]:
    """Get Plays for a Competition

     Retrieve all plays for a given NFL event/competition.

    Args:
        event_id (str):
        competition_id (str):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PlaysListResponse]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            competition_id=competition_id,
            client=client,
            page_index=page_index,
            page_size=page_size,
        )
    ).parsed
