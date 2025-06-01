from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_stats_response import AthleteStatsResponse
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: int,
    *,
    season: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/common/v3/sports/{sport}/{league}/athletes/{athlete_id}/stats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthleteStatsResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AthleteStatsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AthleteStatsResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[AthleteStatsResponse, ErrorResponse]]:
    """Get athlete statistics

     Retrieve detailed career statistics for a specific athlete

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        season=season,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[AthleteStatsResponse, ErrorResponse]]:
    """Get athlete statistics

     Retrieve detailed career statistics for a specific athlete

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatsResponse, ErrorResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        client=client,
        season=season,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[AthleteStatsResponse, ErrorResponse]]:
    """Get athlete statistics

     Retrieve detailed career statistics for a specific athlete

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        season=season,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[AthleteStatsResponse, ErrorResponse]]:
    """Get athlete statistics

     Retrieve detailed career statistics for a specific athlete

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            athlete_id=athlete_id,
            client=client,
            season=season,
        )
    ).parsed
