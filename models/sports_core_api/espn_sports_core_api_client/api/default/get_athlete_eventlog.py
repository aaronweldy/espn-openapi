from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_eventlog_response import AthleteEventlogResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: str,
    league: str,
    year: int,
    athlete_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/athletes/{athlete_id}/eventlog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthleteEventlogResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AthleteEventlogResponse.from_dict(response.json())

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
) -> Response[Union[AthleteEventlogResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: str,
    league: str,
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Response[Union[AthleteEventlogResponse, ErrorResponse]]:
    """Get Athlete Event Log

     Retrieve the event log for a specific athlete in a given season. Shows all events/games the athlete
    participated in during the season.

    Args:
        sport (str):  Example: golf.
        league (str):  Example: pga.
        year (int):  Example: 2024.
        athlete_id (str):  Example: 388.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteEventlogResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: str,
    league: str,
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Optional[Union[AthleteEventlogResponse, ErrorResponse]]:
    """Get Athlete Event Log

     Retrieve the event log for a specific athlete in a given season. Shows all events/games the athlete
    participated in during the season.

    Args:
        sport (str):  Example: golf.
        league (str):  Example: pga.
        year (int):  Example: 2024.
        athlete_id (str):  Example: 388.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteEventlogResponse, ErrorResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
        client=client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    sport: str,
    league: str,
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Response[Union[AthleteEventlogResponse, ErrorResponse]]:
    """Get Athlete Event Log

     Retrieve the event log for a specific athlete in a given season. Shows all events/games the athlete
    participated in during the season.

    Args:
        sport (str):  Example: golf.
        league (str):  Example: pga.
        year (int):  Example: 2024.
        athlete_id (str):  Example: 388.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteEventlogResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: str,
    league: str,
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Optional[Union[AthleteEventlogResponse, ErrorResponse]]:
    """Get Athlete Event Log

     Retrieve the event log for a specific athlete in a given season. Shows all events/games the athlete
    participated in during the season.

    Args:
        sport (str):  Example: golf.
        league (str):  Example: pga.
        year (int):  Example: 2024.
        athlete_id (str):  Example: 388.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteEventlogResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            year=year,
            athlete_id=athlete_id,
            client=client,
            page=page,
            limit=limit,
        )
    ).parsed
