from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.fantasy_team_response import FantasyTeamResponse
from ...models.get_fantasy_football_team_view import GetFantasyFootballTeamView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    segment: int,
    league_id: int,
    team_id: int,
    *,
    view: Union[Unset, GetFantasyFootballTeamView] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_view: Union[Unset, str] = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{league_id}/teams/{team_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FantasyTeamResponse]]:
    if response.status_code == 200:
        response_200 = FantasyTeamResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
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
) -> Response[Union[ErrorResponse, FantasyTeamResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    segment: int,
    league_id: int,
    team_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballTeamView] = UNSET,
) -> Response[Union[ErrorResponse, FantasyTeamResponse]]:
    """Get Fantasy Football Team

     Retrieve detailed information for a specific fantasy football team

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        team_id (int):  Example: 1.
        view (Union[Unset, GetFantasyFootballTeamView]):  Example: mRoster.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyTeamResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        segment=segment,
        league_id=league_id,
        team_id=team_id,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    segment: int,
    league_id: int,
    team_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballTeamView] = UNSET,
) -> Optional[Union[ErrorResponse, FantasyTeamResponse]]:
    """Get Fantasy Football Team

     Retrieve detailed information for a specific fantasy football team

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        team_id (int):  Example: 1.
        view (Union[Unset, GetFantasyFootballTeamView]):  Example: mRoster.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyTeamResponse]
    """

    return sync_detailed(
        year=year,
        segment=segment,
        league_id=league_id,
        team_id=team_id,
        client=client,
        view=view,
    ).parsed


async def asyncio_detailed(
    year: int,
    segment: int,
    league_id: int,
    team_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballTeamView] = UNSET,
) -> Response[Union[ErrorResponse, FantasyTeamResponse]]:
    """Get Fantasy Football Team

     Retrieve detailed information for a specific fantasy football team

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        team_id (int):  Example: 1.
        view (Union[Unset, GetFantasyFootballTeamView]):  Example: mRoster.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyTeamResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        segment=segment,
        league_id=league_id,
        team_id=team_id,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    segment: int,
    league_id: int,
    team_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballTeamView] = UNSET,
) -> Optional[Union[ErrorResponse, FantasyTeamResponse]]:
    """Get Fantasy Football Team

     Retrieve detailed information for a specific fantasy football team

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        team_id (int):  Example: 1.
        view (Union[Unset, GetFantasyFootballTeamView]):  Example: mRoster.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyTeamResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            segment=segment,
            league_id=league_id,
            team_id=team_id,
            client=client,
            view=view,
        )
    ).parsed
