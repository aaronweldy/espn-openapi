from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_notes_response import AthleteNotesResponse
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...types import Response


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    athlete_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/seasons/{year}/athletes/{athlete_id}/notes",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthleteNotesResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AthleteNotesResponse.from_dict(response.json())

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
) -> Response[Union[AthleteNotesResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteNotesResponse, ErrorResponse]]:
    """Get Athlete Season Notes

     Retrieve notes for a specific athlete in a specific season. Notes typically include news updates,
    injury reports, and other relevant information.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):  Example: 2025.
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteNotesResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteNotesResponse, ErrorResponse]]:
    """Get Athlete Season Notes

     Retrieve notes for a specific athlete in a specific season. Notes typically include news updates,
    injury reports, and other relevant information.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):  Example: 2025.
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteNotesResponse, ErrorResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteNotesResponse, ErrorResponse]]:
    """Get Athlete Season Notes

     Retrieve notes for a specific athlete in a specific season. Notes typically include news updates,
    injury reports, and other relevant information.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):  Example: 2025.
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteNotesResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    year: str,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteNotesResponse, ErrorResponse]]:
    """Get Athlete Season Notes

     Retrieve notes for a specific athlete in a specific season. Notes typically include news updates,
    injury reports, and other relevant information.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        year (str):  Example: 2025.
        athlete_id (str):  Example: 3139477.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteNotesResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            year=year,
            athlete_id=athlete_id,
            client=client,
        )
    ).parsed
