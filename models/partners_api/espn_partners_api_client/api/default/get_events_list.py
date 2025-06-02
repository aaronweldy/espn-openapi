from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.events_list_response import EventsListResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    limit: Union[Unset, int] = 100,
    dates: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["dates"] = dates

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/{league}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, EventsListResponse]]:
    if response.status_code == 200:
        response_200 = EventsListResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, EventsListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    dates: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventsListResponse]]:
    """Get Events List

     Retrieve a paginated list of events (games/matches) for a specific sport and league.
    This endpoint supports flexible date filtering.

    Args:
        sport (SportEnum): Sport identifier
        league (LeagueEnum): League identifier
        limit (Union[Unset, int]):  Default: 100. Example: 100.
        dates (Union[Unset, str]):  Example: 20250901-20250907.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventsListResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        limit=limit,
        dates=dates,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    dates: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventsListResponse]]:
    """Get Events List

     Retrieve a paginated list of events (games/matches) for a specific sport and league.
    This endpoint supports flexible date filtering.

    Args:
        sport (SportEnum): Sport identifier
        league (LeagueEnum): League identifier
        limit (Union[Unset, int]):  Default: 100. Example: 100.
        dates (Union[Unset, str]):  Example: 20250901-20250907.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventsListResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        limit=limit,
        dates=dates,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    dates: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventsListResponse]]:
    """Get Events List

     Retrieve a paginated list of events (games/matches) for a specific sport and league.
    This endpoint supports flexible date filtering.

    Args:
        sport (SportEnum): Sport identifier
        league (LeagueEnum): League identifier
        limit (Union[Unset, int]):  Default: 100. Example: 100.
        dates (Union[Unset, str]):  Example: 20250901-20250907.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventsListResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        limit=limit,
        dates=dates,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    dates: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventsListResponse]]:
    """Get Events List

     Retrieve a paginated list of events (games/matches) for a specific sport and league.
    This endpoint supports flexible date filtering.

    Args:
        sport (SportEnum): Sport identifier
        league (LeagueEnum): League identifier
        limit (Union[Unset, int]):  Default: 100. Example: 100.
        dates (Union[Unset, str]):  Example: 20250901-20250907.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventsListResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            limit=limit,
            dates=dates,
        )
    ).parsed
