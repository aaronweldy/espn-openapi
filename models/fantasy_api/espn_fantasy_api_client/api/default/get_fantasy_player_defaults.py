from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.fantasy_player_defaults_response import FantasyPlayerDefaultsResponse
from ...models.get_fantasy_player_defaults_view import GetFantasyPlayerDefaultsView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    segment: int,
    scoring_period_id: int,
    *,
    view: Union[Unset, GetFantasyPlayerDefaultsView] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_fantasy_filter, Unset):
        headers["X-Fantasy-Filter"] = x_fantasy_filter

    params: Dict[str, Any] = {}

    json_view: Union[Unset, str] = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leaguedefaults/{scoring_period_id}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]:
    if response.status_code == 200:
        response_200 = FantasyPlayerDefaultsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    segment: int,
    scoring_period_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyPlayerDefaultsView] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]:
    """Get Fantasy Player Details with Defaults

     Retrieve detailed fantasy player information with league default settings.
    This endpoint returns player data with additional fantasy-specific information
    like draft values, keeper values, and ratings.

    Args:
        year (int):  Example: 2025.
        segment (int):
        scoring_period_id (int):  Example: 1.
        view (Union[Unset, GetFantasyPlayerDefaultsView]):  Example: kona_player_info.
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":50,"sortDraftRanks":{"
            sortPriority":100,"sortAsc":true,"value":"STANDARD"}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        segment=segment,
        scoring_period_id=scoring_period_id,
        view=view,
        x_fantasy_filter=x_fantasy_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    segment: int,
    scoring_period_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyPlayerDefaultsView] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]:
    """Get Fantasy Player Details with Defaults

     Retrieve detailed fantasy player information with league default settings.
    This endpoint returns player data with additional fantasy-specific information
    like draft values, keeper values, and ratings.

    Args:
        year (int):  Example: 2025.
        segment (int):
        scoring_period_id (int):  Example: 1.
        view (Union[Unset, GetFantasyPlayerDefaultsView]):  Example: kona_player_info.
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":50,"sortDraftRanks":{"
            sortPriority":100,"sortAsc":true,"value":"STANDARD"}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyPlayerDefaultsResponse]
    """

    return sync_detailed(
        year=year,
        segment=segment,
        scoring_period_id=scoring_period_id,
        client=client,
        view=view,
        x_fantasy_filter=x_fantasy_filter,
    ).parsed


async def asyncio_detailed(
    year: int,
    segment: int,
    scoring_period_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyPlayerDefaultsView] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]:
    """Get Fantasy Player Details with Defaults

     Retrieve detailed fantasy player information with league default settings.
    This endpoint returns player data with additional fantasy-specific information
    like draft values, keeper values, and ratings.

    Args:
        year (int):  Example: 2025.
        segment (int):
        scoring_period_id (int):  Example: 1.
        view (Union[Unset, GetFantasyPlayerDefaultsView]):  Example: kona_player_info.
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":50,"sortDraftRanks":{"
            sortPriority":100,"sortAsc":true,"value":"STANDARD"}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        segment=segment,
        scoring_period_id=scoring_period_id,
        view=view,
        x_fantasy_filter=x_fantasy_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    segment: int,
    scoring_period_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyPlayerDefaultsView] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FantasyPlayerDefaultsResponse]]:
    """Get Fantasy Player Details with Defaults

     Retrieve detailed fantasy player information with league default settings.
    This endpoint returns player data with additional fantasy-specific information
    like draft values, keeper values, and ratings.

    Args:
        year (int):  Example: 2025.
        segment (int):
        scoring_period_id (int):  Example: 1.
        view (Union[Unset, GetFantasyPlayerDefaultsView]):  Example: kona_player_info.
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":50,"sortDraftRanks":{"
            sortPriority":100,"sortAsc":true,"value":"STANDARD"}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyPlayerDefaultsResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            segment=segment,
            scoring_period_id=scoring_period_id,
            client=client,
            view=view,
            x_fantasy_filter=x_fantasy_filter,
        )
    ).parsed
