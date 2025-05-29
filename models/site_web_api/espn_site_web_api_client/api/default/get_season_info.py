from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.season_info_response import SeasonInfoResponse
from ...models.sport_enum import SportEnum
from ...types import Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/common/v3/sports/{sport}/{league}/season",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SeasonInfoResponse]]:
    if response.status_code == 200:
        response_200 = SeasonInfoResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SeasonInfoResponse]]:
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
) -> Response[Union[ErrorResponse, SeasonInfoResponse]]:
    """Get season information

     Retrieve season information including year, dates, and season types for a specific sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SeasonInfoResponse]]
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
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, SeasonInfoResponse]]:
    """Get season information

     Retrieve season information including year, dates, and season types for a specific sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SeasonInfoResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, SeasonInfoResponse]]:
    """Get season information

     Retrieve season information including year, dates, and season types for a specific sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SeasonInfoResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, SeasonInfoResponse]]:
    """Get season information

     Retrieve season information including year, dates, and season types for a specific sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SeasonInfoResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
        )
    ).parsed
