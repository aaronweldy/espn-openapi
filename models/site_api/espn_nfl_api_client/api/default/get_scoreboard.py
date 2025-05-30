from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.generic_scoreboard_response import GenericScoreboardResponse
from ...models.get_scoreboard_seasontype import GetScoreboardSeasontype
from ...models.get_scoreboard_sport import GetScoreboardSport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: GetScoreboardSport,
    league: str,
    *,
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetScoreboardSeasontype] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["dates"] = dates

    params["week"] = week

    json_seasontype: Union[Unset, int] = UNSET
    if not isinstance(seasontype, Unset):
        json_seasontype = seasontype.value

    params["seasontype"] = json_seasontype

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/{sport}/{league}/scoreboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GenericScoreboardResponse]]:
    if response.status_code == 200:
        response_200 = GenericScoreboardResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GenericScoreboardResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: GetScoreboardSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetScoreboardSeasontype] = UNSET,
) -> Response[Union[ErrorResponse, GenericScoreboardResponse]]:
    """Get Scoreboard

     Retrieve current scoreboard for any sport/league including game scores, status, and basic
    information

    Args:
        sport (GetScoreboardSport):  Example: football.
        league (str):  Example: nfl.
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GenericScoreboardResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        dates=dates,
        week=week,
        seasontype=seasontype,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: GetScoreboardSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetScoreboardSeasontype] = UNSET,
) -> Optional[Union[ErrorResponse, GenericScoreboardResponse]]:
    """Get Scoreboard

     Retrieve current scoreboard for any sport/league including game scores, status, and basic
    information

    Args:
        sport (GetScoreboardSport):  Example: football.
        league (str):  Example: nfl.
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GenericScoreboardResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        dates=dates,
        week=week,
        seasontype=seasontype,
    ).parsed


async def asyncio_detailed(
    sport: GetScoreboardSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetScoreboardSeasontype] = UNSET,
) -> Response[Union[ErrorResponse, GenericScoreboardResponse]]:
    """Get Scoreboard

     Retrieve current scoreboard for any sport/league including game scores, status, and basic
    information

    Args:
        sport (GetScoreboardSport):  Example: football.
        league (str):  Example: nfl.
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GenericScoreboardResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        dates=dates,
        week=week,
        seasontype=seasontype,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: GetScoreboardSport,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetScoreboardSeasontype] = UNSET,
) -> Optional[Union[ErrorResponse, GenericScoreboardResponse]]:
    """Get Scoreboard

     Retrieve current scoreboard for any sport/league including game scores, status, and basic
    information

    Args:
        sport (GetScoreboardSport):  Example: football.
        league (str):  Example: nfl.
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GenericScoreboardResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            dates=dates,
            week=week,
            seasontype=seasontype,
        )
    ).parsed
