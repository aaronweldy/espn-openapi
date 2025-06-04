from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.golf_athlete_stats_response import GolfAthleteStatsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    athlete_id: int,
    *,
    season: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/common/v3/sports/golf/athletes/{athlete_id}/stats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GolfAthleteStatsResponse]]:
    if response.status_code == 200:
        response_200 = GolfAthleteStatsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GolfAthleteStatsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GolfAthleteStatsResponse]]:
    """Get Golf Athlete Statistics

     Retrieve detailed career statistics for a specific golf athlete

    Args:
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GolfAthleteStatsResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
        season=season,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GolfAthleteStatsResponse]]:
    """Get Golf Athlete Statistics

     Retrieve detailed career statistics for a specific golf athlete

    Args:
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GolfAthleteStatsResponse]
    """

    return sync_detailed(
        athlete_id=athlete_id,
        client=client,
        season=season,
    ).parsed


async def asyncio_detailed(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GolfAthleteStatsResponse]]:
    """Get Golf Athlete Statistics

     Retrieve detailed career statistics for a specific golf athlete

    Args:
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GolfAthleteStatsResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
        season=season,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GolfAthleteStatsResponse]]:
    """Get Golf Athlete Statistics

     Retrieve detailed career statistics for a specific golf athlete

    Args:
        athlete_id (int):
        season (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GolfAthleteStatsResponse]
    """

    return (
        await asyncio_detailed(
            athlete_id=athlete_id,
            client=client,
            season=season,
        )
    ).parsed
