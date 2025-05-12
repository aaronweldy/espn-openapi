from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.game_summary import GameSummary
from ...types import UNSET, Response


def _get_kwargs(
    *,
    event: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["event"] = event

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sports/football/nfl/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GameSummary]]:
    if response.status_code == 200:
        response_200 = GameSummary.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GameSummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Response[Union[ErrorResponse, GameSummary]]:
    """Get NFL Game Summary

     Retrieve comprehensive summary data for a specific NFL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GameSummary]]
    """

    kwargs = _get_kwargs(
        event=event,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Optional[Union[ErrorResponse, GameSummary]]:
    """Get NFL Game Summary

     Retrieve comprehensive summary data for a specific NFL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GameSummary]
    """

    return sync_detailed(
        client=client,
        event=event,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Response[Union[ErrorResponse, GameSummary]]:
    """Get NFL Game Summary

     Retrieve comprehensive summary data for a specific NFL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GameSummary]]
    """

    kwargs = _get_kwargs(
        event=event,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Optional[Union[ErrorResponse, GameSummary]]:
    """Get NFL Game Summary

     Retrieve comprehensive summary data for a specific NFL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401547417.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GameSummary]
    """

    return (
        await asyncio_detailed(
            client=client,
            event=event,
        )
    ).parsed
