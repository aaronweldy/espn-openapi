from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.soccer_standings_response import SoccerStandingsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    league: str,
    *,
    season: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/soccer/{league}/standings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SoccerStandingsResponse]]:
    if response.status_code == 200:
        response_200 = SoccerStandingsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, SoccerStandingsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SoccerStandingsResponse]]:
    """Get Soccer League Standings

     Retrieve current standings for a soccer league including table positions, points, and statistics

    Args:
        league (str):  Example: eng.1.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SoccerStandingsResponse]]
    """

    kwargs = _get_kwargs(
        league=league,
        season=season,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SoccerStandingsResponse]]:
    """Get Soccer League Standings

     Retrieve current standings for a soccer league including table positions, points, and statistics

    Args:
        league (str):  Example: eng.1.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SoccerStandingsResponse]
    """

    return sync_detailed(
        league=league,
        client=client,
        season=season,
    ).parsed


async def asyncio_detailed(
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SoccerStandingsResponse]]:
    """Get Soccer League Standings

     Retrieve current standings for a soccer league including table positions, points, and statistics

    Args:
        league (str):  Example: eng.1.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SoccerStandingsResponse]]
    """

    kwargs = _get_kwargs(
        league=league,
        season=season,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SoccerStandingsResponse]]:
    """Get Soccer League Standings

     Retrieve current standings for a soccer league including table positions, points, and statistics

    Args:
        league (str):  Example: eng.1.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SoccerStandingsResponse]
    """

    return (
        await asyncio_detailed(
            league=league,
            client=client,
            season=season,
        )
    ).parsed
