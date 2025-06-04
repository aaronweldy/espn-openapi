from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.probability_item import ProbabilityItem
from ...models.sport_enum import SportEnum
from ...types import Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    play_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/probabilities/{play_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ProbabilityItem]]:
    if response.status_code == 200:
        response_200 = ProbabilityItem.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ProbabilityItem]]:
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
    play_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, ProbabilityItem]]:
    """Get Play Probability

     Retrieve win probability data for a specific play in a game. Shows the probability of each team
    winning at the moment of this specific play.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        play_id (str):  Example: 4015474171.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ProbabilityItem]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        play_id=play_id,
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
    play_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, ProbabilityItem]]:
    """Get Play Probability

     Retrieve win probability data for a specific play in a game. Shows the probability of each team
    winning at the moment of this specific play.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        play_id (str):  Example: 4015474171.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ProbabilityItem]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        play_id=play_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    play_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, ProbabilityItem]]:
    """Get Play Probability

     Retrieve win probability data for a specific play in a game. Shows the probability of each team
    winning at the moment of this specific play.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        play_id (str):  Example: 4015474171.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ProbabilityItem]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        play_id=play_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    play_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, ProbabilityItem]]:
    """Get Play Probability

     Retrieve win probability data for a specific play in a game. Shows the probability of each team
    winning at the moment of this specific play.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):  Example: 401547417.
        competition_id (str):  Example: 401547417.
        play_id (str):  Example: 4015474171.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ProbabilityItem]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=competition_id,
            play_id=play_id,
            client=client,
        )
    ).parsed
