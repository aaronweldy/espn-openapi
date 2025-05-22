from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.nhl_scoreboard_response import NhlScoreboardResponse
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
        "url": "/sports/hockey/nhl/scoreboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NhlScoreboardResponse]]:
    if response.status_code == 200:
        response_200 = NhlScoreboardResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NhlScoreboardResponse]]:
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
) -> Response[Union[ErrorResponse, NhlScoreboardResponse]]:
    """Get NHL Scoreboard

     Retrieve current NHL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240601.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NhlScoreboardResponse]]
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
) -> Optional[Union[ErrorResponse, NhlScoreboardResponse]]:
    """Get NHL Scoreboard

     Retrieve current NHL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240601.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NhlScoreboardResponse]
    """

    return sync_detailed(
        client=client,
        dates=dates,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dates: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, NhlScoreboardResponse]]:
    """Get NHL Scoreboard

     Retrieve current NHL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240601.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NhlScoreboardResponse]]
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
) -> Optional[Union[ErrorResponse, NhlScoreboardResponse]]:
    """Get NHL Scoreboard

     Retrieve current NHL scoreboard including game scores, status, and basic information

    Args:
        dates (Union[Unset, str]):  Example: 20240601.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NhlScoreboardResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            dates=dates,
        )
    ).parsed
