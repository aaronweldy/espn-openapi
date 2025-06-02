from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...models.team_athletes_response import TeamAthletesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    team_id: str,
    *,
    active: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["active"] = active

    params["pageIndex"] = page_index

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/teams/{team_id}/athletes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TeamAthletesResponse]]:
    if response.status_code == 200:
        response_200 = TeamAthletesResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, TeamAthletesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, TeamAthletesResponse]]:
    """Get Team Athletes

     Retrieve athletes for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):
        team_id (str):
        active (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamAthletesResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        team_id=team_id,
        active=active,
        page_index=page_index,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, TeamAthletesResponse]]:
    """Get Team Athletes

     Retrieve athletes for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):
        team_id (str):
        active (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamAthletesResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        year=year,
        team_id=team_id,
        client=client,
        active=active,
        page_index=page_index,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, TeamAthletesResponse]]:
    """Get Team Athletes

     Retrieve athletes for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):
        team_id (str):
        active (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamAthletesResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        team_id=team_id,
        active=active,
        page_index=page_index,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, TeamAthletesResponse]]:
    """Get Team Athletes

     Retrieve athletes for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):
        team_id (str):
        active (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamAthletesResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            year=year,
            team_id=team_id,
            client=client,
            active=active,
            page_index=page_index,
            limit=limit,
        )
    ).parsed
