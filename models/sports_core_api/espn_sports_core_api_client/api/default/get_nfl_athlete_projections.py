from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_statistics_response import AthleteStatisticsResponse
from ...models.error_response import ErrorResponse
from ...models.get_nfl_athlete_projections_seasontype import GetNFLAthleteProjectionsSeasontype
from ...types import Response


def _get_kwargs(
    year: int,
    seasontype: GetNFLAthleteProjectionsSeasontype,
    athlete_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/athletes/{athlete_id}/projections",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AthleteStatisticsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    seasontype: GetNFLAthleteProjectionsSeasontype,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Projections

     Retrieve projected statistics for an NFL athlete for a specific season and season type.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLAthleteProjectionsSeasontype):  Example: 2.
        athlete_id (str):  Example: 4040715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        seasontype=seasontype,
        athlete_id=athlete_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    seasontype: GetNFLAthleteProjectionsSeasontype,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Projections

     Retrieve projected statistics for an NFL athlete for a specific season and season type.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLAthleteProjectionsSeasontype):  Example: 2.
        athlete_id (str):  Example: 4040715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatisticsResponse, ErrorResponse]
    """

    return sync_detailed(
        year=year,
        seasontype=seasontype,
        athlete_id=athlete_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    year: int,
    seasontype: GetNFLAthleteProjectionsSeasontype,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Projections

     Retrieve projected statistics for an NFL athlete for a specific season and season type.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLAthleteProjectionsSeasontype):  Example: 2.
        athlete_id (str):  Example: 4040715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        seasontype=seasontype,
        athlete_id=athlete_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    seasontype: GetNFLAthleteProjectionsSeasontype,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Projections

     Retrieve projected statistics for an NFL athlete for a specific season and season type.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLAthleteProjectionsSeasontype):  Example: 2.
        athlete_id (str):  Example: 4040715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatisticsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            seasontype=seasontype,
            athlete_id=athlete_id,
            client=client,
        )
    ).parsed
