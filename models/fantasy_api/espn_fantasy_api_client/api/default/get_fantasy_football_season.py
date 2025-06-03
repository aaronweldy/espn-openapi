from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.fantasy_season_response import FantasySeasonResponse
from ...models.get_fantasy_football_season_view import GetFantasyFootballSeasonView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    *,
    view: Union[Unset, GetFantasyFootballSeasonView] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_view: Union[Unset, str] = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v3/games/ffl/seasons/{year}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FantasySeasonResponse]]:
    if response.status_code == 200:
        response_200 = FantasySeasonResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, FantasySeasonResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballSeasonView] = UNSET,
) -> Response[Union[ErrorResponse, FantasySeasonResponse]]:
    """Get Fantasy Football Season Data

     Retrieve season-level data for fantasy football, including pro team schedules and bye weeks

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballSeasonView]):  Example: proTeamSchedules_wl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasySeasonResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballSeasonView] = UNSET,
) -> Optional[Union[ErrorResponse, FantasySeasonResponse]]:
    """Get Fantasy Football Season Data

     Retrieve season-level data for fantasy football, including pro team schedules and bye weeks

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballSeasonView]):  Example: proTeamSchedules_wl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasySeasonResponse]
    """

    return sync_detailed(
        year=year,
        client=client,
        view=view,
    ).parsed


async def asyncio_detailed(
    year: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballSeasonView] = UNSET,
) -> Response[Union[ErrorResponse, FantasySeasonResponse]]:
    """Get Fantasy Football Season Data

     Retrieve season-level data for fantasy football, including pro team schedules and bye weeks

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballSeasonView]):  Example: proTeamSchedules_wl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasySeasonResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballSeasonView] = UNSET,
) -> Optional[Union[ErrorResponse, FantasySeasonResponse]]:
    """Get Fantasy Football Season Data

     Retrieve season-level data for fantasy football, including pro team schedules and bye weeks

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballSeasonView]):  Example: proTeamSchedules_wl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasySeasonResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            client=client,
            view=view,
        )
    ).parsed
