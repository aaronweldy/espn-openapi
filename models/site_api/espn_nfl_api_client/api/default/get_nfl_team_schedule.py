from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.nfl_team_schedule_response import NFLTeamScheduleResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    season: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/football/nfl/teams/{team_id}/schedule",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NFLTeamScheduleResponse]]:
    if response.status_code == 200:
        response_200 = NFLTeamScheduleResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NFLTeamScheduleResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, NFLTeamScheduleResponse]]:
    """Get NFL Team Schedule

     Retrieve the full schedule for a specific NFL team, including all games for the season.

    Args:
        team_id (str):  Example: 12.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NFLTeamScheduleResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        season=season,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, NFLTeamScheduleResponse]]:
    """Get NFL Team Schedule

     Retrieve the full schedule for a specific NFL team, including all games for the season.

    Args:
        team_id (str):  Example: 12.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NFLTeamScheduleResponse]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        season=season,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, NFLTeamScheduleResponse]]:
    """Get NFL Team Schedule

     Retrieve the full schedule for a specific NFL team, including all games for the season.

    Args:
        team_id (str):  Example: 12.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NFLTeamScheduleResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        season=season,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, NFLTeamScheduleResponse]]:
    """Get NFL Team Schedule

     Retrieve the full schedule for a specific NFL team, including all games for the season.

    Args:
        team_id (str):  Example: 12.
        season (Union[Unset, int]):  Example: 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NFLTeamScheduleResponse]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            season=season,
        )
    ).parsed
