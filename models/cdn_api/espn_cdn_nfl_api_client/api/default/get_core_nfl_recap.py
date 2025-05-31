from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nfl_recap_response import NflRecapResponse
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
        "url": "/core/nfl/recap",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NflRecapResponse]:
    if response.status_code == 200:
        response_200 = NflRecapResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NflRecapResponse]:
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
) -> Response[NflRecapResponse]:
    """NFL Game Recap

     Get the NFL game recap data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflRecapResponse]
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
) -> Optional[NflRecapResponse]:
    """NFL Game Recap

     Get the NFL game recap data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflRecapResponse
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
) -> Response[NflRecapResponse]:
    """NFL Game Recap

     Get the NFL game recap data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflRecapResponse]
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
) -> Optional[NflRecapResponse]:
    """NFL Game Recap

     Get the NFL game recap data.

    Args:
        xhr (int):
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflRecapResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            xhr=xhr,
            game_id=game_id,
        )
    ).parsed
