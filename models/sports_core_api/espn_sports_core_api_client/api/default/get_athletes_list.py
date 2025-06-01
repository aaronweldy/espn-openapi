from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athletes_list_response import AthletesListResponse
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    page_index: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 25,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/athletes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthletesListResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AthletesListResponse.from_dict(response.json())

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
) -> Response[Union[AthletesListResponse, ErrorResponse]]:
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
    page_index: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 25,
) -> Response[Union[AthletesListResponse, ErrorResponse]]:
    """List Athletes

     Retrieve a paginated list of athletes for a specific sport and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        page_index (Union[Unset, int]):  Default: 1. Example: 1.
        page_size (Union[Unset, int]):  Default: 25. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthletesListResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        page_index=page_index,
        page_size=page_size,
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
    page_index: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 25,
) -> Optional[Union[AthletesListResponse, ErrorResponse]]:
    """List Athletes

     Retrieve a paginated list of athletes for a specific sport and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        page_index (Union[Unset, int]):  Default: 1. Example: 1.
        page_size (Union[Unset, int]):  Default: 25. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthletesListResponse, ErrorResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        page_index=page_index,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 25,
) -> Response[Union[AthletesListResponse, ErrorResponse]]:
    """List Athletes

     Retrieve a paginated list of athletes for a specific sport and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        page_index (Union[Unset, int]):  Default: 1. Example: 1.
        page_size (Union[Unset, int]):  Default: 25. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthletesListResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        page_index=page_index,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 25,
) -> Optional[Union[AthletesListResponse, ErrorResponse]]:
    """List Athletes

     Retrieve a paginated list of athletes for a specific sport and league.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        page_index (Union[Unset, int]):  Default: 1. Example: 1.
        page_size (Union[Unset, int]):  Default: 25. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthletesListResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            page_index=page_index,
            page_size=page_size,
        )
    ).parsed
