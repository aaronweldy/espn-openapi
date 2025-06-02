from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...models.team_odds_records_response import TeamOddsRecordsResponse
from ...types import Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    seasontype: int,
    team_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/teams/{team_id}/odds-records",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TeamOddsRecordsResponse]]:
    if response.status_code == 200:
        response_200 = TeamOddsRecordsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, TeamOddsRecordsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    seasontype: int,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, TeamOddsRecordsResponse]]:
    """Get Team Odds Records

     Retrieve comprehensive odds records for a specific team in a given season, including money line
    and spread performance broken down by various categories (overall, home, away, underdog, favorite).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamOddsRecordsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    seasontype: int,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, TeamOddsRecordsResponse]]:
    """Get Team Odds Records

     Retrieve comprehensive odds records for a specific team in a given season, including money line
    and spread performance broken down by various categories (overall, home, away, underdog, favorite).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamOddsRecordsResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    seasontype: int,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, TeamOddsRecordsResponse]]:
    """Get Team Odds Records

     Retrieve comprehensive odds records for a specific team in a given season, including money line
    and spread performance broken down by various categories (overall, home, away, underdog, favorite).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamOddsRecordsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    seasontype: int,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, TeamOddsRecordsResponse]]:
    """Get Team Odds Records

     Retrieve comprehensive odds records for a specific team in a given season, including money line
    and spread performance broken down by various categories (overall, home, away, underdog, favorite).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamOddsRecordsResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            year=year,
            seasontype=seasontype,
            team_id=team_id,
            client=client,
        )
    ).parsed
