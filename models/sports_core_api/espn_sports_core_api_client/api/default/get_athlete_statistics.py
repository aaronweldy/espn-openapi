from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_statistics_response import AthleteStatisticsResponse
from ...models.error_response import ErrorResponse
from ...models.get_athlete_statistics_seasontype import GetAthleteStatisticsSeasontype
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: str,
    *,
    limit: Union[Unset, int] = 100,
    seasontype: Union[Unset, GetAthleteStatisticsSeasontype] = UNSET,
    year: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    json_seasontype: Union[Unset, int] = UNSET
    if not isinstance(seasontype, Unset):
        json_seasontype = seasontype.value

    params["seasontype"] = json_seasontype

    params["year"] = year

    params["week"] = week

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AthleteStatisticsResponse.from_dict(response.json())

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
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    seasontype: Union[Unset, GetAthleteStatisticsSeasontype] = UNSET,
    year: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get Athlete Statistics

     Retrieve detailed statistics for a specific athlete in any supported sport/league. Query parameters
    allow filtering by season, week, and season type.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (str):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 100.
        seasontype (Union[Unset, GetAthleteStatisticsSeasontype]):
        year (Union[Unset, int]):
        week (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        limit=limit,
        seasontype=seasontype,
        year=year,
        week=week,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    seasontype: Union[Unset, GetAthleteStatisticsSeasontype] = UNSET,
    year: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get Athlete Statistics

     Retrieve detailed statistics for a specific athlete in any supported sport/league. Query parameters
    allow filtering by season, week, and season type.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (str):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 100.
        seasontype (Union[Unset, GetAthleteStatisticsSeasontype]):
        year (Union[Unset, int]):
        week (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatisticsResponse, ErrorResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        client=client,
        limit=limit,
        seasontype=seasontype,
        year=year,
        week=week,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    seasontype: Union[Unset, GetAthleteStatisticsSeasontype] = UNSET,
    year: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get Athlete Statistics

     Retrieve detailed statistics for a specific athlete in any supported sport/league. Query parameters
    allow filtering by season, week, and season type.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (str):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 100.
        seasontype (Union[Unset, GetAthleteStatisticsSeasontype]):
        year (Union[Unset, int]):
        week (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        limit=limit,
        seasontype=seasontype,
        year=year,
        week=week,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    seasontype: Union[Unset, GetAthleteStatisticsSeasontype] = UNSET,
    year: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get Athlete Statistics

     Retrieve detailed statistics for a specific athlete in any supported sport/league. Query parameters
    allow filtering by season, week, and season type.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (str):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 100.
        seasontype (Union[Unset, GetAthleteStatisticsSeasontype]):
        year (Union[Unset, int]):
        week (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatisticsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            athlete_id=athlete_id,
            client=client,
            limit=limit,
            seasontype=seasontype,
            year=year,
            week=week,
        )
    ).parsed
