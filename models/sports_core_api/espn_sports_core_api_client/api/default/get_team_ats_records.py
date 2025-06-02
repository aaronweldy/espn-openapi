from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...models.team_ats_records_response import TeamAtsRecordsResponse
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
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/teams/{team_id}/ats",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TeamAtsRecordsResponse]]:
    if response.status_code == 200:
        response_200 = TeamAtsRecordsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, TeamAtsRecordsResponse]]:
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
) -> Response[Union[ErrorResponse, TeamAtsRecordsResponse]]:
    """Get Team ATS Records

     Retrieve Against The Spread (ATS) records for a specific team in a given season.

    **Note**: This endpoint is only supported for sports with variable point spreads (NFL, NBA).
    MLB and NHL will return 500 errors as they use fixed spreads (run line and puck line respectively).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2023.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamAtsRecordsResponse]]
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
) -> Optional[Union[ErrorResponse, TeamAtsRecordsResponse]]:
    """Get Team ATS Records

     Retrieve Against The Spread (ATS) records for a specific team in a given season.

    **Note**: This endpoint is only supported for sports with variable point spreads (NFL, NBA).
    MLB and NHL will return 500 errors as they use fixed spreads (run line and puck line respectively).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2023.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamAtsRecordsResponse]
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
) -> Response[Union[ErrorResponse, TeamAtsRecordsResponse]]:
    """Get Team ATS Records

     Retrieve Against The Spread (ATS) records for a specific team in a given season.

    **Note**: This endpoint is only supported for sports with variable point spreads (NFL, NBA).
    MLB and NHL will return 500 errors as they use fixed spreads (run line and puck line respectively).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2023.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamAtsRecordsResponse]]
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
) -> Optional[Union[ErrorResponse, TeamAtsRecordsResponse]]:
    """Get Team ATS Records

     Retrieve Against The Spread (ATS) records for a specific team in a given season.

    **Note**: This endpoint is only supported for sports with variable point spreads (NFL, NBA).
    MLB and NHL will return 500 errors as they use fixed spreads (run line and puck line respectively).

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2023.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamAtsRecordsResponse]
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
