from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_players_response import AvailablePlayersResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    segment: int,
    league_id: int,
    *,
    scoring_period_id: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["scoringPeriodId"] = scoring_period_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{league_id}/players/available",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AvailablePlayersResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AvailablePlayersResponse.from_dict(response.json())

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
) -> Response[Union[AvailablePlayersResponse, ErrorResponse]]:
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
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
) -> Response[Union[AvailablePlayersResponse, ErrorResponse]]:
    """Get Available Players

     Retrieve list of available players in a fantasy football league

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        scoring_period_id (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailablePlayersResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        segment=segment,
        league_id=league_id,
        scoring_period_id=scoring_period_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    segment: int,
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
) -> Optional[Union[AvailablePlayersResponse, ErrorResponse]]:
    """Get Available Players

     Retrieve list of available players in a fantasy football league

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        scoring_period_id (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AvailablePlayersResponse, ErrorResponse]
    """

    return sync_detailed(
        year=year,
        segment=segment,
        league_id=league_id,
        client=client,
        scoring_period_id=scoring_period_id,
    ).parsed


async def asyncio_detailed(
    year: int,
    segment: int,
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
) -> Response[Union[AvailablePlayersResponse, ErrorResponse]]:
    """Get Available Players

     Retrieve list of available players in a fantasy football league

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        scoring_period_id (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailablePlayersResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        segment=segment,
        league_id=league_id,
        scoring_period_id=scoring_period_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    segment: int,
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
) -> Optional[Union[AvailablePlayersResponse, ErrorResponse]]:
    """Get Available Players

     Retrieve list of available players in a fantasy football league

    Args:
        year (int):  Example: 2023.
        segment (int):
        league_id (int):  Example: 12345678.
        scoring_period_id (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AvailablePlayersResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            segment=segment,
            league_id=league_id,
            client=client,
            scoring_period_id=scoring_period_id,
        )
    ).parsed
