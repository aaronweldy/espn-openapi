from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...models.team_past_performances_response import TeamPastPerformancesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    team_id: str,
    provider_id: str,
    *,
    limit: Union[Unset, int] = 25,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/teams/{team_id}/odds/{provider_id}/past-performances",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TeamPastPerformancesResponse]]:
    if response.status_code == 200:
        response_200 = TeamPastPerformancesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, TeamPastPerformancesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    team_id: str,
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
) -> Response[Union[ErrorResponse, TeamPastPerformancesResponse]]:
    """Get Team Past Performances vs Odds

     Retrieve historical betting performance data for a specific team against odds from a specific
    provider.
    Shows how the team performed against the spread, money line, and over/under betting lines.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id (str):  Example: 8.
        provider_id (str):  Example: 1002.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamPastPerformancesResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        team_id=team_id,
        provider_id=provider_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    team_id: str,
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
) -> Optional[Union[ErrorResponse, TeamPastPerformancesResponse]]:
    """Get Team Past Performances vs Odds

     Retrieve historical betting performance data for a specific team against odds from a specific
    provider.
    Shows how the team performed against the spread, money line, and over/under betting lines.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id (str):  Example: 8.
        provider_id (str):  Example: 1002.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamPastPerformancesResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        team_id=team_id,
        provider_id=provider_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    team_id: str,
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
) -> Response[Union[ErrorResponse, TeamPastPerformancesResponse]]:
    """Get Team Past Performances vs Odds

     Retrieve historical betting performance data for a specific team against odds from a specific
    provider.
    Shows how the team performed against the spread, money line, and over/under betting lines.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id (str):  Example: 8.
        provider_id (str):  Example: 1002.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TeamPastPerformancesResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        team_id=team_id,
        provider_id=provider_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    team_id: str,
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
) -> Optional[Union[ErrorResponse, TeamPastPerformancesResponse]]:
    """Get Team Past Performances vs Odds

     Retrieve historical betting performance data for a specific team against odds from a specific
    provider.
    Shows how the team performed against the spread, money line, and over/under betting lines.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        team_id (str):  Example: 8.
        provider_id (str):  Example: 1002.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TeamPastPerformancesResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            team_id=team_id,
            provider_id=provider_id,
            client=client,
            limit=limit,
        )
    ).parsed
