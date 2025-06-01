from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.odds_item import OddsItem
from ...models.sport_enum import SportEnum
from ...types import Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    provider_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds/{provider_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, OddsItem]]:
    if response.status_code == 200:
        response_200 = OddsItem.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, OddsItem]]:
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
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, OddsItem]]:
    """Get Competition Odds from Specific Provider

     Retrieve betting odds from a specific provider for a competition within an event for a given sport
    and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OddsItem]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
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
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, OddsItem]]:
    """Get Competition Odds from Specific Provider

     Retrieve betting odds from a specific provider for a competition within an event for a given sport
    and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OddsItem]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, OddsItem]]:
    """Get Competition Odds from Specific Provider

     Retrieve betting odds from a specific provider for a competition within an event for a given sport
    and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OddsItem]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    provider_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, OddsItem]]:
    """Get Competition Odds from Specific Provider

     Retrieve betting odds from a specific provider for a competition within an event for a given sport
    and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OddsItem]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=competition_id,
            provider_id=provider_id,
            client=client,
        )
    ).parsed
