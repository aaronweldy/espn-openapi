from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_nfl_conference_standings_seasontype import GetNFLConferenceStandingsSeasontype
from ...models.nfl_conference_standings_response import NflConferenceStandingsResponse
from ...types import Response


def _get_kwargs(
    year: int,
    seasontype: GetNFLConferenceStandingsSeasontype,
    group_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/groups/{group_id}/standings",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NflConferenceStandingsResponse]]:
    if response.status_code == 200:
        response_200 = NflConferenceStandingsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NflConferenceStandingsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    seasontype: GetNFLConferenceStandingsSeasontype,
    group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, NflConferenceStandingsResponse]]:
    """Get NFL Conference Standings

     Retrieve NFL conference standings for a given year, season type, and group (e.g., NFC or AFC).

    Args:
        year (int):  Example: 2023.
        seasontype (GetNFLConferenceStandingsSeasontype):  Example: 2.
        group_id (int):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NflConferenceStandingsResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        seasontype=seasontype,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    seasontype: GetNFLConferenceStandingsSeasontype,
    group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, NflConferenceStandingsResponse]]:
    """Get NFL Conference Standings

     Retrieve NFL conference standings for a given year, season type, and group (e.g., NFC or AFC).

    Args:
        year (int):  Example: 2023.
        seasontype (GetNFLConferenceStandingsSeasontype):  Example: 2.
        group_id (int):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NflConferenceStandingsResponse]
    """

    return sync_detailed(
        year=year,
        seasontype=seasontype,
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    year: int,
    seasontype: GetNFLConferenceStandingsSeasontype,
    group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, NflConferenceStandingsResponse]]:
    """Get NFL Conference Standings

     Retrieve NFL conference standings for a given year, season type, and group (e.g., NFC or AFC).

    Args:
        year (int):  Example: 2023.
        seasontype (GetNFLConferenceStandingsSeasontype):  Example: 2.
        group_id (int):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NflConferenceStandingsResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        seasontype=seasontype,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    seasontype: GetNFLConferenceStandingsSeasontype,
    group_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, NflConferenceStandingsResponse]]:
    """Get NFL Conference Standings

     Retrieve NFL conference standings for a given year, season type, and group (e.g., NFC or AFC).

    Args:
        year (int):  Example: 2023.
        seasontype (GetNFLConferenceStandingsSeasontype):  Example: 2.
        group_id (int):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NflConferenceStandingsResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            seasontype=seasontype,
            group_id=group_id,
            client=client,
        )
    ).parsed
