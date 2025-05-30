from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.scoreboard_header_response import ScoreboardHeaderResponse
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response


def _get_kwargs(
    *,
    sport: SportEnum,
    league: LeagueEnum,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_sport = sport.value
    params["sport"] = json_sport

    json_league = league.value
    params["league"] = json_league

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/apis/v2/scoreboard/header",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ScoreboardHeaderResponse]]:
    if response.status_code == 200:
        response_200 = ScoreboardHeaderResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ScoreboardHeaderResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sport: SportEnum,
    league: LeagueEnum,
) -> Response[Union[ErrorResponse, ScoreboardHeaderResponse]]:
    """Get Scoreboard Header

     Retrieve header information for scoreboard pages

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ScoreboardHeaderResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sport: SportEnum,
    league: LeagueEnum,
) -> Optional[Union[ErrorResponse, ScoreboardHeaderResponse]]:
    """Get Scoreboard Header

     Retrieve header information for scoreboard pages

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ScoreboardHeaderResponse]
    """

    return sync_detailed(
        client=client,
        sport=sport,
        league=league,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sport: SportEnum,
    league: LeagueEnum,
) -> Response[Union[ErrorResponse, ScoreboardHeaderResponse]]:
    """Get Scoreboard Header

     Retrieve header information for scoreboard pages

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ScoreboardHeaderResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    sport: SportEnum,
    league: LeagueEnum,
) -> Optional[Union[ErrorResponse, ScoreboardHeaderResponse]]:
    """Get Scoreboard Header

     Retrieve header information for scoreboard pages

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ScoreboardHeaderResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            sport=sport,
            league=league,
        )
    ).parsed
