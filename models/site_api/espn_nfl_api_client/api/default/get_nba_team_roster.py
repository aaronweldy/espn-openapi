from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.nba_team_abbreviation import NBATeamAbbreviation
from ...models.nba_team_roster_response import NBATeamRosterResponse
from ...types import Response


def _get_kwargs(
    team_id_or_abbrev: Union[NBATeamAbbreviation, str],
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/basketball/nba/teams/{team_id_or_abbrev}/roster",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NBATeamRosterResponse]]:
    if response.status_code == 200:
        response_200 = NBATeamRosterResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NBATeamRosterResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id_or_abbrev: Union[NBATeamAbbreviation, str],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, NBATeamRosterResponse]]:
    """Get NBA Team Roster

     Retrieve detailed roster information for a specific NBA team including player details

    Args:
        team_id_or_abbrev (Union[NBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NBATeamRosterResponse]]
    """

    kwargs = _get_kwargs(
        team_id_or_abbrev=team_id_or_abbrev,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id_or_abbrev: Union[NBATeamAbbreviation, str],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, NBATeamRosterResponse]]:
    """Get NBA Team Roster

     Retrieve detailed roster information for a specific NBA team including player details

    Args:
        team_id_or_abbrev (Union[NBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NBATeamRosterResponse]
    """

    return sync_detailed(
        team_id_or_abbrev=team_id_or_abbrev,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id_or_abbrev: Union[NBATeamAbbreviation, str],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, NBATeamRosterResponse]]:
    """Get NBA Team Roster

     Retrieve detailed roster information for a specific NBA team including player details

    Args:
        team_id_or_abbrev (Union[NBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NBATeamRosterResponse]]
    """

    kwargs = _get_kwargs(
        team_id_or_abbrev=team_id_or_abbrev,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id_or_abbrev: Union[NBATeamAbbreviation, str],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, NBATeamRosterResponse]]:
    """Get NBA Team Roster

     Retrieve detailed roster information for a specific NBA team including player details

    Args:
        team_id_or_abbrev (Union[NBATeamAbbreviation, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NBATeamRosterResponse]
    """

    return (
        await asyncio_detailed(
            team_id_or_abbrev=team_id_or_abbrev,
            client=client,
        )
    ).parsed
