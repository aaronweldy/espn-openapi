from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_league_season_corrections_season_type import GetLeagueSeasonCorrectionsSeasonType
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...models.stat_corrections_response import StatCorrectionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    season_type: GetLeagueSeasonCorrectionsSeasonType,
    *,
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["lang"] = lang

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/corrections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, StatCorrectionsResponse]]:
    if response.status_code == 200:
        response_200 = StatCorrectionsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, StatCorrectionsResponse]]:
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
    season_type: GetLeagueSeasonCorrectionsSeasonType,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, StatCorrectionsResponse]]:
    """Get League Season Stat Corrections

     Retrieve the list of statistical corrections for a given season and season type in a league and
    sport. Returns a paginated list of stat correction records.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        season_type (GetLeagueSeasonCorrectionsSeasonType):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, StatCorrectionsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        season_type=season_type,
        lang=lang,
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    season_type: GetLeagueSeasonCorrectionsSeasonType,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, StatCorrectionsResponse]]:
    """Get League Season Stat Corrections

     Retrieve the list of statistical corrections for a given season and season type in a league and
    sport. Returns a paginated list of stat correction records.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        season_type (GetLeagueSeasonCorrectionsSeasonType):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, StatCorrectionsResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        year=year,
        season_type=season_type,
        client=client,
        lang=lang,
        region=region,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    season_type: GetLeagueSeasonCorrectionsSeasonType,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, StatCorrectionsResponse]]:
    """Get League Season Stat Corrections

     Retrieve the list of statistical corrections for a given season and season type in a league and
    sport. Returns a paginated list of stat correction records.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        season_type (GetLeagueSeasonCorrectionsSeasonType):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, StatCorrectionsResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        season_type=season_type,
        lang=lang,
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    year: int,
    season_type: GetLeagueSeasonCorrectionsSeasonType,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, StatCorrectionsResponse]]:
    """Get League Season Stat Corrections

     Retrieve the list of statistical corrections for a given season and season type in a league and
    sport. Returns a paginated list of stat correction records.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (int):  Example: 2024.
        season_type (GetLeagueSeasonCorrectionsSeasonType):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, StatCorrectionsResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            year=year,
            season_type=season_type,
            client=client,
            lang=lang,
            region=region,
        )
    ).parsed
