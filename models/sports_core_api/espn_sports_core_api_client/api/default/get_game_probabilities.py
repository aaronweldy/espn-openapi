from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.probabilities_list_response import ProbabilitiesListResponse
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    *,
    limit: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/probabilities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ProbabilitiesListResponse]]:
    if response.status_code == 200:
        response_200 = ProbabilitiesListResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ProbabilitiesListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Response[Union[ErrorResponse, ProbabilitiesListResponse]]:
    """Get Game Win Probabilities

     Retrieve win probability data for each play in a game. Shows how the probability of each team
    winning changed throughout the game.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        limit (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ProbabilitiesListResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        limit=limit,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Optional[Union[ErrorResponse, ProbabilitiesListResponse]]:
    """Get Game Win Probabilities

     Retrieve win probability data for each play in a game. Shows how the probability of each team
    winning changed throughout the game.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        limit (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ProbabilitiesListResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=client,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Response[Union[ErrorResponse, ProbabilitiesListResponse]]:
    """Get Game Win Probabilities

     Retrieve win probability data for each play in a game. Shows how the probability of each team
    winning changed throughout the game.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        limit (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ProbabilitiesListResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Optional[Union[ErrorResponse, ProbabilitiesListResponse]]:
    """Get Game Win Probabilities

     Retrieve win probability data for each play in a game. Shows how the probability of each team
    winning changed throughout the game.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        limit (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ProbabilitiesListResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=competition_id,
            client=client,
            limit=limit,
            page=page,
        )
    ).parsed
