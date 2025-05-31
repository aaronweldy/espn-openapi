from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nfl_game_response import NflGameResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    xhr: int,
    game_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["xhr"] = xhr

    params["gameId"] = game_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/core/nfl/game",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NflGameResponse]:
    if response.status_code == 200:
        response_200 = NflGameResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NflGameResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    xhr: int,
    game_id: str,
) -> Response[NflGameResponse]:
    """NFL Game Details

     Get the NFL game details data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflGameResponse]
    """

    kwargs = _get_kwargs(
        xhr=xhr,
        game_id=game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    xhr: int,
    game_id: str,
) -> Optional[NflGameResponse]:
    """NFL Game Details

     Get the NFL game details data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflGameResponse
    """

    return sync_detailed(
        client=client,
        xhr=xhr,
        game_id=game_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    xhr: int,
    game_id: str,
) -> Response[NflGameResponse]:
    """NFL Game Details

     Get the NFL game details data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflGameResponse]
    """

    kwargs = _get_kwargs(
        xhr=xhr,
        game_id=game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    xhr: int,
    game_id: str,
) -> Optional[NflGameResponse]:
    """NFL Game Details

     Get the NFL game details data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflGameResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            xhr=xhr,
            game_id=game_id,
        )
    ).parsed
