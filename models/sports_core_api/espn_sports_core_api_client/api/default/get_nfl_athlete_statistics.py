from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_statistics_response import AthleteStatisticsResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    athlete_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/football/leagues/nfl/athletes/{athlete_id}/statistics",
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
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
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
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Statistics

     Retrieve detailed statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Statistics

     Retrieve detailed statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatisticsResponse, ErrorResponse]
    """

    return sync_detailed(
        athlete_id=athlete_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Statistics

     Retrieve detailed statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteStatisticsResponse, ErrorResponse]]:
    """Get NFL Athlete Statistics

     Retrieve detailed statistics for a specific NFL athlete

    Args:
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteStatisticsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            athlete_id=athlete_id,
            client=client,
        )
    ).parsed
