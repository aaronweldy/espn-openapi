from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nfl_boxscore_response import NflBoxscoreResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    xhr: int,
    gameid: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["xhr"] = xhr

    params["gameid"] = gameid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/core/nfl/boxscore",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NflBoxscoreResponse]:
    if response.status_code == 200:
        response_200 = NflBoxscoreResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NflBoxscoreResponse]:
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
    gameid: str,
) -> Response[NflBoxscoreResponse]:
    """NFL Boxscore

     Get the NFL boxscore data for a game.

    Args:
        xhr (int):
        gameid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflBoxscoreResponse]
    """

    kwargs = _get_kwargs(
        xhr=xhr,
        gameid=gameid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    xhr: int,
    gameid: str,
) -> Optional[NflBoxscoreResponse]:
    """NFL Boxscore

     Get the NFL boxscore data for a game.

    Args:
        xhr (int):
        gameid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflBoxscoreResponse
    """

    return sync_detailed(
        client=client,
        xhr=xhr,
        gameid=gameid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    xhr: int,
    gameid: str,
) -> Response[NflBoxscoreResponse]:
    """NFL Boxscore

     Get the NFL boxscore data for a game.

    Args:
        xhr (int):
        gameid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflBoxscoreResponse]
    """

    kwargs = _get_kwargs(
        xhr=xhr,
        gameid=gameid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    xhr: int,
    gameid: str,
) -> Optional[NflBoxscoreResponse]:
    """NFL Boxscore

     Get the NFL boxscore data for a game.

    Args:
        xhr (int):
        gameid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflBoxscoreResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            xhr=xhr,
            gameid=gameid,
        )
    ).parsed
