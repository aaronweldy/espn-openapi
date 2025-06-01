from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.fantasy_player_news_response import FantasyPlayerNewsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    player_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["playerId"] = player_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/fantasy/v2/games/ffl/news/players",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FantasyPlayerNewsResponse]]:
    if response.status_code == 200:
        response_200 = FantasyPlayerNewsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, FantasyPlayerNewsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    player_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, FantasyPlayerNewsResponse]]:
    """Get Fantasy Football Player News

     Retrieve fantasy football news articles for players. Can be filtered by player ID.

    Args:
        player_id (Union[Unset, int]):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyPlayerNewsResponse]]
    """

    kwargs = _get_kwargs(
        player_id=player_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    player_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, FantasyPlayerNewsResponse]]:
    """Get Fantasy Football Player News

     Retrieve fantasy football news articles for players. Can be filtered by player ID.

    Args:
        player_id (Union[Unset, int]):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyPlayerNewsResponse]
    """

    return sync_detailed(
        client=client,
        player_id=player_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    player_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, FantasyPlayerNewsResponse]]:
    """Get Fantasy Football Player News

     Retrieve fantasy football news articles for players. Can be filtered by player ID.

    Args:
        player_id (Union[Unset, int]):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FantasyPlayerNewsResponse]]
    """

    kwargs = _get_kwargs(
        player_id=player_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    player_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, FantasyPlayerNewsResponse]]:
    """Get Fantasy Football Player News

     Retrieve fantasy football news articles for players. Can be filtered by player ID.

    Args:
        player_id (Union[Unset, int]):  Example: 3139477.
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FantasyPlayerNewsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            player_id=player_id,
            limit=limit,
        )
    ).parsed
