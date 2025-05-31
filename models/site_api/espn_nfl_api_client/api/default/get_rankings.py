from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_rankings_league import GetRankingsLeague
from ...models.get_rankings_sport import GetRankingsSport
from ...models.rankings_response import RankingsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: GetRankingsSport,
    league: GetRankingsLeague,
    *,
    season: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    params["week"] = week

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/{sport}/{league}/rankings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, RankingsResponse]]:
    if response.status_code == 200:
        response_200 = RankingsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, RankingsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: GetRankingsSport,
    league: GetRankingsLeague,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, RankingsResponse]]:
    """Get Rankings

     Retrieve current rankings/polls for college sports (AP Top 25, Coaches Poll, etc.). Only available
    for college sports.

    Args:
        sport (GetRankingsSport):  Example: football.
        league (GetRankingsLeague):  Example: college-football.
        season (Union[Unset, int]):  Example: 2024.
        week (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RankingsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        season=season,
        week=week,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: GetRankingsSport,
    league: GetRankingsLeague,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, RankingsResponse]]:
    """Get Rankings

     Retrieve current rankings/polls for college sports (AP Top 25, Coaches Poll, etc.). Only available
    for college sports.

    Args:
        sport (GetRankingsSport):  Example: football.
        league (GetRankingsLeague):  Example: college-football.
        season (Union[Unset, int]):  Example: 2024.
        week (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RankingsResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        season=season,
        week=week,
    ).parsed


async def asyncio_detailed(
    sport: GetRankingsSport,
    league: GetRankingsLeague,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, RankingsResponse]]:
    """Get Rankings

     Retrieve current rankings/polls for college sports (AP Top 25, Coaches Poll, etc.). Only available
    for college sports.

    Args:
        sport (GetRankingsSport):  Example: football.
        league (GetRankingsLeague):  Example: college-football.
        season (Union[Unset, int]):  Example: 2024.
        week (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RankingsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        season=season,
        week=week,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: GetRankingsSport,
    league: GetRankingsLeague,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    week: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, RankingsResponse]]:
    """Get Rankings

     Retrieve current rankings/polls for college sports (AP Top 25, Coaches Poll, etc.). Only available
    for college sports.

    Args:
        sport (GetRankingsSport):  Example: football.
        league (GetRankingsLeague):  Example: college-football.
        season (Union[Unset, int]):  Example: 2024.
        week (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RankingsResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            season=season,
            week=week,
        )
    ).parsed
