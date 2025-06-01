from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.coach_details_response import CoachDetailsResponse
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...types import Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    coach_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/coaches/{coach_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CoachDetailsResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CoachDetailsResponse.from_dict(response.json())

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
) -> Response[Union[CoachDetailsResponse, ErrorResponse]]:
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
    coach_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CoachDetailsResponse, ErrorResponse]]:
    """Get Season Coach Details

     Retrieve details for a specific coach in a given sport, league, and season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        coach_id (str):  Example: 17751.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CoachDetailsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        coach_id=coach_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    coach_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CoachDetailsResponse, ErrorResponse]]:
    """Get Season Coach Details

     Retrieve details for a specific coach in a given sport, league, and season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        coach_id (str):  Example: 17751.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CoachDetailsResponse, ErrorResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        year=year,
        coach_id=coach_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    coach_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CoachDetailsResponse, ErrorResponse]]:
    """Get Season Coach Details

     Retrieve details for a specific coach in a given sport, league, and season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        coach_id (str):  Example: 17751.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CoachDetailsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        coach_id=coach_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    coach_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CoachDetailsResponse, ErrorResponse]]:
    """Get Season Coach Details

     Retrieve details for a specific coach in a given sport, league, and season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        coach_id (str):  Example: 17751.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CoachDetailsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            year=year,
            coach_id=coach_id,
            client=client,
        )
    ).parsed
