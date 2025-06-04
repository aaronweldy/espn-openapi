from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.fantasy_player import FantasyPlayer
from ...models.get_fantasy_football_players_view import GetFantasyFootballPlayersView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    *,
    view: Union[Unset, GetFantasyFootballPlayersView] = UNSET,
    scoring_period_id: Union[Unset, int] = UNSET,
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

    params["scoringPeriodId"] = scoring_period_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v3/games/ffl/seasons/{year}/players",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, List["FantasyPlayer"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FantasyPlayer.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[ErrorResponse, List["FantasyPlayer"]]]:
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
    view: Union[Unset, GetFantasyFootballPlayersView] = UNSET,
    scoring_period_id: Union[Unset, int] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, List["FantasyPlayer"]]]:
    """Get Fantasy Football Players

     Retrieve a list of fantasy football players with various statistics and information.

    Note: The X-Fantasy-Filter header can be used to limit the number of players returned.
    Without it, the API returns all players (typically 2000+). The limit in the filter
    doesn't always work as expected - some views ignore it and return all players.

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballPlayersView]):  Example: kona_player_info.
        scoring_period_id (Union[Unset, int]):
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":3000}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, List['FantasyPlayer']]]
    """

    kwargs = _get_kwargs(
        year=year,
        view=view,
        scoring_period_id=scoring_period_id,
        x_fantasy_filter=x_fantasy_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballPlayersView] = UNSET,
    scoring_period_id: Union[Unset, int] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, List["FantasyPlayer"]]]:
    """Get Fantasy Football Players

     Retrieve a list of fantasy football players with various statistics and information.

    Note: The X-Fantasy-Filter header can be used to limit the number of players returned.
    Without it, the API returns all players (typically 2000+). The limit in the filter
    doesn't always work as expected - some views ignore it and return all players.

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballPlayersView]):  Example: kona_player_info.
        scoring_period_id (Union[Unset, int]):
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":3000}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, List['FantasyPlayer']]
    """

    return sync_detailed(
        year=year,
        client=client,
        view=view,
        scoring_period_id=scoring_period_id,
        x_fantasy_filter=x_fantasy_filter,
    ).parsed


async def asyncio_detailed(
    year: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballPlayersView] = UNSET,
    scoring_period_id: Union[Unset, int] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, List["FantasyPlayer"]]]:
    """Get Fantasy Football Players

     Retrieve a list of fantasy football players with various statistics and information.

    Note: The X-Fantasy-Filter header can be used to limit the number of players returned.
    Without it, the API returns all players (typically 2000+). The limit in the filter
    doesn't always work as expected - some views ignore it and return all players.

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballPlayersView]):  Example: kona_player_info.
        scoring_period_id (Union[Unset, int]):
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":3000}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, List['FantasyPlayer']]]
    """

    kwargs = _get_kwargs(
        year=year,
        view=view,
        scoring_period_id=scoring_period_id,
        x_fantasy_filter=x_fantasy_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetFantasyFootballPlayersView] = UNSET,
    scoring_period_id: Union[Unset, int] = UNSET,
    x_fantasy_filter: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, List["FantasyPlayer"]]]:
    """Get Fantasy Football Players

     Retrieve a list of fantasy football players with various statistics and information.

    Note: The X-Fantasy-Filter header can be used to limit the number of players returned.
    Without it, the API returns all players (typically 2000+). The limit in the filter
    doesn't always work as expected - some views ignore it and return all players.

    Args:
        year (int):  Example: 2024.
        view (Union[Unset, GetFantasyFootballPlayersView]):  Example: kona_player_info.
        scoring_period_id (Union[Unset, int]):
        x_fantasy_filter (Union[Unset, str]):  Example: {"players":{"limit":3000}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, List['FantasyPlayer']]
    """

    return (
        await asyncio_detailed(
            year=year,
            client=client,
            view=view,
            scoring_period_id=scoring_period_id,
            x_fantasy_filter=x_fantasy_filter,
        )
    ).parsed
