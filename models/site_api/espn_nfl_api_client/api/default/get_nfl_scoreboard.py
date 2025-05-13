from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_nfl_scoreboard_seasontype import GetNFLScoreboardSeasontype
from ...models.scoreboard import Scoreboard
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLScoreboardSeasontype] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["dates"] = dates

    params["week"] = week

    json_seasontype: Union[Unset, int] = UNSET
    if not isinstance(seasontype, Unset):
        json_seasontype = seasontype.value

    params["seasontype"] = json_seasontype

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sports/football/nfl/scoreboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, Scoreboard]]:
    if response.status_code == 200:
        response_200 = Scoreboard.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, Scoreboard]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLScoreboardSeasontype] = UNSET,
) -> Response[Union[ErrorResponse, Scoreboard]]:
    """Get NFL Scoreboard

     Retrieve current NFL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetNFLScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Scoreboard]]
    """

    kwargs = _get_kwargs(
        dates=dates,
        week=week,
        seasontype=seasontype,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLScoreboardSeasontype] = UNSET,
) -> Optional[Union[ErrorResponse, Scoreboard]]:
    """Get NFL Scoreboard

     Retrieve current NFL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetNFLScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Scoreboard]
    """

    return sync_detailed(
        client=client,
        dates=dates,
        week=week,
        seasontype=seasontype,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLScoreboardSeasontype] = UNSET,
) -> Response[Union[ErrorResponse, Scoreboard]]:
    """Get NFL Scoreboard

     Retrieve current NFL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetNFLScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Scoreboard]]
    """

    kwargs = _get_kwargs(
        dates=dates,
        week=week,
        seasontype=seasontype,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
    week: Union[Unset, int] = UNSET,
    seasontype: Union[Unset, GetNFLScoreboardSeasontype] = UNSET,
) -> Optional[Union[ErrorResponse, Scoreboard]]:
    """Get NFL Scoreboard

     Retrieve current NFL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240201.
        week (Union[Unset, int]):  Example: 1.
        seasontype (Union[Unset, GetNFLScoreboardSeasontype]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Scoreboard]
    """

    return (
        await asyncio_detailed(
            client=client,
            dates=dates,
            week=week,
            seasontype=seasontype,
        )
    ).parsed
