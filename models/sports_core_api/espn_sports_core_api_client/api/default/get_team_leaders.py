from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...models.team_leaders_response import TeamLeadersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    seasontype: int,
    team_id: str,
    *,
    limit: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/teams/{team_id}/leaders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TeamLeadersResponse]]:
    if response.status_code == 200:
        response_200 = TeamLeadersResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, TeamLeadersResponse]]:
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
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, TeamLeadersResponse]]:
    """Get Team Leaders

     Retrieve statistical leaders for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.
        limit (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamLeadersResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
        limit=limit,
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
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, TeamLeadersResponse]]:
    """Get Team Leaders

     Retrieve statistical leaders for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.
        limit (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamLeadersResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    seasontype: int,
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, TeamLeadersResponse]]:
    """Get Team Leaders

     Retrieve statistical leaders for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.
        limit (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamLeadersResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
        limit=limit,
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
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, TeamLeadersResponse]]:
    """Get Team Leaders

     Retrieve statistical leaders for a specific team in a given season.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        seasontype (int):  Example: 2.
        team_id (str):  Example: 12.
        limit (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamLeadersResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            year=year,
            seasontype=seasontype,
            team_id=team_id,
            client=client,
            limit=limit,
        )
    ).parsed
