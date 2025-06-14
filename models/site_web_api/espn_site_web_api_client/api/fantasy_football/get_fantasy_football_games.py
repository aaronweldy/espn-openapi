from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.fantasy_games_response import FantasyGamesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dates: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["dates"] = dates

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/apis/fantasy/v2/games/ffl/games",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FantasyGamesResponse]]:
    if response.status_code == 200:
        response_200 = FantasyGamesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, FantasyGamesResponse]]:
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
) -> Response[Union[ErrorResponse, FantasyGamesResponse]]:
    """Get Fantasy Football Games

     Retrieve a list of NFL games with fantasy-relevant information

    Args:
        dates (Union[Unset, str]):  Example: 20241201.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyGamesResponse]]
    """

    kwargs = _get_kwargs(
        dates=dates,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FantasyGamesResponse]]:
    """Get Fantasy Football Games

     Retrieve a list of NFL games with fantasy-relevant information

    Args:
        dates (Union[Unset, str]):  Example: 20241201.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyGamesResponse]
    """

    return sync_detailed(
        client=client,
        dates=dates,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FantasyGamesResponse]]:
    """Get Fantasy Football Games

     Retrieve a list of NFL games with fantasy-relevant information

    Args:
        dates (Union[Unset, str]):  Example: 20241201.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyGamesResponse]]
    """

    kwargs = _get_kwargs(
        dates=dates,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FantasyGamesResponse]]:
    """Get Fantasy Football Games

     Retrieve a list of NFL games with fantasy-relevant information

    Args:
        dates (Union[Unset, str]):  Example: 20241201.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyGamesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            dates=dates,
        )
    ).parsed
