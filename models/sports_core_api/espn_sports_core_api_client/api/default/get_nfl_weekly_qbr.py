from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_nfl_weekly_qbr_seasontype import GetNFLWeeklyQBRSeasontype
from ...models.nfl_weekly_qbr_response import NFLWeeklyQBRResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    seasontype: GetNFLWeeklyQBRSeasontype,
    week: int,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/weeks/{week}/qbr/10000",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NFLWeeklyQBRResponse]]:
    if response.status_code == 200:
        response_200 = NFLWeeklyQBRResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NFLWeeklyQBRResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    seasontype: GetNFLWeeklyQBRSeasontype,
    week: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Response[Union[ErrorResponse, NFLWeeklyQBRResponse]]:
    """Get NFL Weekly QBR

     Retrieve quarterback rating (QBR) statistics for all quarterbacks for a specific week in an NFL
    season.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLWeeklyQBRSeasontype):  Example: 2.
        week (int):  Example: 1.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NFLWeeklyQBRResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        seasontype=seasontype,
        week=week,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    seasontype: GetNFLWeeklyQBRSeasontype,
    week: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Optional[Union[ErrorResponse, NFLWeeklyQBRResponse]]:
    """Get NFL Weekly QBR

     Retrieve quarterback rating (QBR) statistics for all quarterbacks for a specific week in an NFL
    season.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLWeeklyQBRSeasontype):  Example: 2.
        week (int):  Example: 1.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NFLWeeklyQBRResponse]
    """

    return sync_detailed(
        year=year,
        seasontype=seasontype,
        week=week,
        client=client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    year: int,
    seasontype: GetNFLWeeklyQBRSeasontype,
    week: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Response[Union[ErrorResponse, NFLWeeklyQBRResponse]]:
    """Get NFL Weekly QBR

     Retrieve quarterback rating (QBR) statistics for all quarterbacks for a specific week in an NFL
    season.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLWeeklyQBRSeasontype):  Example: 2.
        week (int):  Example: 1.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NFLWeeklyQBRResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        seasontype=seasontype,
        week=week,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    seasontype: GetNFLWeeklyQBRSeasontype,
    week: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 25,
) -> Optional[Union[ErrorResponse, NFLWeeklyQBRResponse]]:
    """Get NFL Weekly QBR

     Retrieve quarterback rating (QBR) statistics for all quarterbacks for a specific week in an NFL
    season.

    Args:
        year (int):  Example: 2024.
        seasontype (GetNFLWeeklyQBRSeasontype):  Example: 2.
        week (int):  Example: 1.
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NFLWeeklyQBRResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            seasontype=seasontype,
            week=week,
            client=client,
            page=page,
            limit=limit,
        )
    ).parsed
