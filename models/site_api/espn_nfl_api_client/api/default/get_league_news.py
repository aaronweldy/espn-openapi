from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.sport_enum import SportEnum
from ...models.sport_news_api_schema import SportNewsAPISchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    limit: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["team"] = team

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sports/{sport}/{league}/news",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SportNewsAPISchema]]:
    if response.status_code == 200:
        response_200 = SportNewsAPISchema.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SportNewsAPISchema]]:
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
    limit: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get League News

     Retrieve the latest news articles and headlines for a specified sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        limit (Union[Unset, int]):  Example: 10.
        team (Union[Unset, int]):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SportNewsAPISchema]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        limit=limit,
        team=team,
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
    limit: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get League News

     Retrieve the latest news articles and headlines for a specified sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        limit (Union[Unset, int]):  Example: 10.
        team (Union[Unset, int]):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SportNewsAPISchema]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        limit=limit,
        team=team,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get League News

     Retrieve the latest news articles and headlines for a specified sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        limit (Union[Unset, int]):  Example: 10.
        team (Union[Unset, int]):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SportNewsAPISchema]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        limit=limit,
        team=team,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get League News

     Retrieve the latest news articles and headlines for a specified sport and league

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        limit (Union[Unset, int]):  Example: 10.
        team (Union[Unset, int]):  Example: 12.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SportNewsAPISchema]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            limit=limit,
            team=team,
        )
    ).parsed
