from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_competition_odds_movement_history_type import GetCompetitionOddsMovementHistoryType
from ...models.league_enum import LeagueEnum
from ...models.odds_movement_response import OddsMovementResponse
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    provider_id: str,
    history_type: GetCompetitionOddsMovementHistoryType,
    *,
    limit: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds/{provider_id}/history/{history_type}/movement",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, OddsMovementResponse]]:
    if response.status_code == 200:
        response_200 = OddsMovementResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, OddsMovementResponse]]:
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
    history_type: GetCompetitionOddsMovementHistoryType,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, OddsMovementResponse]]:
    """Get Odds Movement History

     Retrieve detailed historical odds movements for a specific bet type from a provider.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):
        history_type (GetCompetitionOddsMovementHistoryType):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OddsMovementResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
        history_type=history_type,
        limit=limit,
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
    history_type: GetCompetitionOddsMovementHistoryType,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, OddsMovementResponse]]:
    """Get Odds Movement History

     Retrieve detailed historical odds movements for a specific bet type from a provider.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):
        history_type (GetCompetitionOddsMovementHistoryType):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OddsMovementResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
        history_type=history_type,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    provider_id: str,
    history_type: GetCompetitionOddsMovementHistoryType,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, OddsMovementResponse]]:
    """Get Odds Movement History

     Retrieve detailed historical odds movements for a specific bet type from a provider.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):
        history_type (GetCompetitionOddsMovementHistoryType):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OddsMovementResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
        history_type=history_type,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    event_id: str,
    competition_id: str,
    provider_id: str,
    history_type: GetCompetitionOddsMovementHistoryType,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, OddsMovementResponse]]:
    """Get Odds Movement History

     Retrieve detailed historical odds movements for a specific bet type from a provider.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event_id (str):
        competition_id (str):
        provider_id (str):
        history_type (GetCompetitionOddsMovementHistoryType):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OddsMovementResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=competition_id,
            provider_id=provider_id,
            history_type=history_type,
            client=client,
            limit=limit,
        )
    ).parsed
