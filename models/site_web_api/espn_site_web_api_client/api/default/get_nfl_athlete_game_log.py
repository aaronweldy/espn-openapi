from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_game_log_response import AthleteGameLogResponse
from ...models.error_response import ErrorResponse
from ...models.get_nfl_athlete_game_log_seasontype import GetNFLAthleteGameLogSeasontype
from ...types import UNSET, Response, Unset


def _get_kwargs(
    athlete_id: str,
    *,
    season: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLAthleteGameLogSeasontype] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    json_seasontype: Union[Unset, int] = UNSET
    if not isinstance(seasontype, Unset):
        json_seasontype = seasontype.value

    params["seasontype"] = json_seasontype

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/common/v3/sports/football/nfl/athletes/{athlete_id}/gamelog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthleteGameLogResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AthleteGameLogResponse.from_dict(response.json())

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
) -> Response[Union[AthleteGameLogResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLAthleteGameLogSeasontype] = UNSET,
) -> Response[Union[AthleteGameLogResponse, ErrorResponse]]:
    """Get NFL Athlete Game Log

     Retrieve game-by-game statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.
        season (Union[Unset, int]):  Example: 2023.
        seasontype (Union[Unset, GetNFLAthleteGameLogSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteGameLogResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
        season=season,
        seasontype=seasontype,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLAthleteGameLogSeasontype] = UNSET,
) -> Optional[Union[AthleteGameLogResponse, ErrorResponse]]:
    """Get NFL Athlete Game Log

     Retrieve game-by-game statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.
        season (Union[Unset, int]):  Example: 2023.
        seasontype (Union[Unset, GetNFLAthleteGameLogSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteGameLogResponse, ErrorResponse]
    """

    return sync_detailed(
        athlete_id=athlete_id,
        client=client,
        season=season,
        seasontype=seasontype,
    ).parsed


async def asyncio_detailed(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLAthleteGameLogSeasontype] = UNSET,
) -> Response[Union[AthleteGameLogResponse, ErrorResponse]]:
    """Get NFL Athlete Game Log

     Retrieve game-by-game statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.
        season (Union[Unset, int]):  Example: 2023.
        seasontype (Union[Unset, GetNFLAthleteGameLogSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteGameLogResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
        season=season,
        seasontype=seasontype,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLAthleteGameLogSeasontype] = UNSET,
) -> Optional[Union[AthleteGameLogResponse, ErrorResponse]]:
    """Get NFL Athlete Game Log

     Retrieve game-by-game statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.
        season (Union[Unset, int]):  Example: 2023.
        seasontype (Union[Unset, GetNFLAthleteGameLogSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteGameLogResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            athlete_id=athlete_id,
            client=client,
            season=season,
            seasontype=seasontype,
        )
    ).parsed
