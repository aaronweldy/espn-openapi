from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.news_response import NewsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 50,
    sport: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["sport"] = sport

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/sports/news",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NewsResponse]]:
    if response.status_code == 200:
        response_200 = NewsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NewsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    sport: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, NewsResponse]]:
    """Get Sports News

     Retrieve sports news headlines. Can be filtered by sport.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        sport (Union[Unset, str]):  Example: football.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NewsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        sport=sport,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    sport: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, NewsResponse]]:
    """Get Sports News

     Retrieve sports news headlines. Can be filtered by sport.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        sport (Union[Unset, str]):  Example: football.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NewsResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        sport=sport,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    sport: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, NewsResponse]]:
    """Get Sports News

     Retrieve sports news headlines. Can be filtered by sport.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        sport (Union[Unset, str]):  Example: football.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NewsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        sport=sport,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    sport: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, NewsResponse]]:
    """Get Sports News

     Retrieve sports news headlines. Can be filtered by sport.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        sport (Union[Unset, str]):  Example: football.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NewsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            sport=sport,
            offset=offset,
        )
    ).parsed
