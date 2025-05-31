from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.game_summary import GameSummary
from ...models.league_enum import LeagueEnum
from ...models.mlb_game_summary_response import MlbGameSummaryResponse
from ...models.nba_game_summary_response import NbaGameSummaryResponse
from ...models.nhl_game_summary_response import NhlGameSummaryResponse
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    event: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["event"] = event

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/{sport}/{league}/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ErrorResponse,
        Union["GameSummary", "MlbGameSummaryResponse", "NbaGameSummaryResponse", "NhlGameSummaryResponse"],
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["GameSummary", "MlbGameSummaryResponse", "NbaGameSummaryResponse", "NhlGameSummaryResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GameSummary.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = MlbGameSummaryResponse.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = NhlGameSummaryResponse.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_3 = NbaGameSummaryResponse.from_dict(data)

            return response_200_type_3

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    Union[
        ErrorResponse,
        Union["GameSummary", "MlbGameSummaryResponse", "NbaGameSummaryResponse", "NhlGameSummaryResponse"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Response[
    Union[
        ErrorResponse,
        Union["GameSummary", "MlbGameSummaryResponse", "NbaGameSummaryResponse", "NhlGameSummaryResponse"],
    ]
]:
    """Get Game Summary

     Retrieve comprehensive summary data for a specific game including scores, statistics, and detailed
    game information

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['GameSummary', 'MlbGameSummaryResponse', 'NbaGameSummaryResponse', 'NhlGameSummaryResponse']]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event=event,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Optional[
    Union[
        ErrorResponse,
        Union["GameSummary", "MlbGameSummaryResponse", "NbaGameSummaryResponse", "NhlGameSummaryResponse"],
    ]
]:
    """Get Game Summary

     Retrieve comprehensive summary data for a specific game including scores, statistics, and detailed
    game information

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['GameSummary', 'MlbGameSummaryResponse', 'NbaGameSummaryResponse', 'NhlGameSummaryResponse']]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        event=event,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Response[
    Union[
        ErrorResponse,
        Union["GameSummary", "MlbGameSummaryResponse", "NbaGameSummaryResponse", "NhlGameSummaryResponse"],
    ]
]:
    """Get Game Summary

     Retrieve comprehensive summary data for a specific game including scores, statistics, and detailed
    game information

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['GameSummary', 'MlbGameSummaryResponse', 'NbaGameSummaryResponse', 'NhlGameSummaryResponse']]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        event=event,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Optional[
    Union[
        ErrorResponse,
        Union["GameSummary", "MlbGameSummaryResponse", "NbaGameSummaryResponse", "NhlGameSummaryResponse"],
    ]
]:
    """Get Game Summary

     Retrieve comprehensive summary data for a specific game including scores, statistics, and detailed
    game information

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['GameSummary', 'MlbGameSummaryResponse', 'NbaGameSummaryResponse', 'NhlGameSummaryResponse']]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            event=event,
        )
    ).parsed
