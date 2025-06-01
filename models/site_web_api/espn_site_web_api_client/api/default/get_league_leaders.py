from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_league_leaders_sport import GetLeagueLeadersSport
from ...models.leaders_response import LeadersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: GetLeagueLeadersSport,
    league: str,
    *,
    season: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/site/v3/sports/{sport}/{league}/leaders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, LeadersResponse]]:
    if response.status_code == 200:
        response_200 = LeadersResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, LeadersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: GetLeagueLeadersSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, LeadersResponse]]:
    """Get League Leaders

     Get statistical leaders for a specific sport and league (NFL, NHL, college sports, etc.)

    Args:
        sport (GetLeagueLeadersSport):
        league (str):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LeadersResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        season=season,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: GetLeagueLeadersSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, LeadersResponse]]:
    """Get League Leaders

     Get statistical leaders for a specific sport and league (NFL, NHL, college sports, etc.)

    Args:
        sport (GetLeagueLeadersSport):
        league (str):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LeadersResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        season=season,
    ).parsed


async def asyncio_detailed(
    sport: GetLeagueLeadersSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, LeadersResponse]]:
    """Get League Leaders

     Get statistical leaders for a specific sport and league (NFL, NHL, college sports, etc.)

    Args:
        sport (GetLeagueLeadersSport):
        league (str):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LeadersResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        season=season,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: GetLeagueLeadersSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, LeadersResponse]]:
    """Get League Leaders

     Get statistical leaders for a specific sport and league (NFL, NHL, college sports, etc.)

    Args:
        sport (GetLeagueLeadersSport):
        league (str):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LeadersResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            season=season,
        )
    ).parsed
