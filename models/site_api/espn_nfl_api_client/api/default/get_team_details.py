from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.mlb_team_abbreviation import MLBTeamAbbreviation
from ...models.nba_team_abbreviation import NBATeamAbbreviation
from ...models.nfl_team_abbreviation import NFLTeamAbbreviation
from ...models.nhl_team_abbreviation import NHLTeamAbbreviation
from ...models.sport_enum import SportEnum
from ...models.team_details_response import TeamDetailsResponse
from ...models.wnba_team_abbreviation import WNBATeamAbbreviation
from ...types import Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    team_id_or_abbrev: Union[
        MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation, NHLTeamAbbreviation, WNBATeamAbbreviation, str
    ],
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/{sport}/{league}/teams/{team_id_or_abbrev}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TeamDetailsResponse]]:
    if response.status_code == 200:
        response_200 = TeamDetailsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, TeamDetailsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    team_id_or_abbrev: Union[
        MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation, NHLTeamAbbreviation, WNBATeamAbbreviation, str
    ],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, TeamDetailsResponse]]:
    """Get Team Details

     Retrieve detailed information for a specific team by ID or abbreviation

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id_or_abbrev (Union[MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation,
            NHLTeamAbbreviation, WNBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamDetailsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        team_id_or_abbrev=team_id_or_abbrev,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    team_id_or_abbrev: Union[
        MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation, NHLTeamAbbreviation, WNBATeamAbbreviation, str
    ],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, TeamDetailsResponse]]:
    """Get Team Details

     Retrieve detailed information for a specific team by ID or abbreviation

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id_or_abbrev (Union[MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation,
            NHLTeamAbbreviation, WNBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamDetailsResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        team_id_or_abbrev=team_id_or_abbrev,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    team_id_or_abbrev: Union[
        MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation, NHLTeamAbbreviation, WNBATeamAbbreviation, str
    ],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, TeamDetailsResponse]]:
    """Get Team Details

     Retrieve detailed information for a specific team by ID or abbreviation

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id_or_abbrev (Union[MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation,
            NHLTeamAbbreviation, WNBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamDetailsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        team_id_or_abbrev=team_id_or_abbrev,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    team_id_or_abbrev: Union[
        MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation, NHLTeamAbbreviation, WNBATeamAbbreviation, str
    ],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, TeamDetailsResponse]]:
    """Get Team Details

     Retrieve detailed information for a specific team by ID or abbreviation

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id_or_abbrev (Union[MLBTeamAbbreviation, NBATeamAbbreviation, NFLTeamAbbreviation,
            NHLTeamAbbreviation, WNBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamDetailsResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            team_id_or_abbrev=team_id_or_abbrev,
            client=client,
        )
    ).parsed
