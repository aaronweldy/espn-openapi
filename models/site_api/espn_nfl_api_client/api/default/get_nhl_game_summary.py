from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.nhl_game_summary_response import NhlGameSummaryResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    event: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["event"] = event

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sports/hockey/nhl/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NhlGameSummaryResponse]]:
    if response.status_code == 200:
        response_200 = NhlGameSummaryResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NhlGameSummaryResponse]]:
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
) -> Response[Union[ErrorResponse, NhlGameSummaryResponse]]:
    """Get NHL Game Summary

     Retrieve comprehensive summary data for a specific NHL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401559593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NhlGameSummaryResponse]]
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
) -> Optional[Union[ErrorResponse, NhlGameSummaryResponse]]:
    """Get NHL Game Summary

     Retrieve comprehensive summary data for a specific NHL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401559593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NhlGameSummaryResponse]
    """

    return sync_detailed(
        client=client,
        event=event,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event: str,
) -> Response[Union[ErrorResponse, NhlGameSummaryResponse]]:
    """Get NHL Game Summary

     Retrieve comprehensive summary data for a specific NHL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401559593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NhlGameSummaryResponse]]
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
) -> Optional[Union[ErrorResponse, NhlGameSummaryResponse]]:
    """Get NHL Game Summary

     Retrieve comprehensive summary data for a specific NHL game including scores, statistics, and
    detailed game information

    Args:
        event (str):  Example: 401559593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NhlGameSummaryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            event=event,
        )
    ).parsed
