from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.search_v2_response import SearchV2Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    limit: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query"] = query

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/apis/search/v2",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SearchV2Response]]:
    if response.status_code == 200:
        response_200 = SearchV2Response.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SearchV2Response]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SearchV2Response]]:
    """General Search (v2)

     Search for sports content including teams, athletes, articles and more (legacy v2 endpoint)

    Args:
        query (str):  Example: Tom Brady.
        limit (Union[Unset, int]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SearchV2Response]]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SearchV2Response]]:
    """General Search (v2)

     Search for sports content including teams, athletes, articles and more (legacy v2 endpoint)

    Args:
        query (str):  Example: Tom Brady.
        limit (Union[Unset, int]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SearchV2Response]
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SearchV2Response]]:
    """General Search (v2)

     Search for sports content including teams, athletes, articles and more (legacy v2 endpoint)

    Args:
        query (str):  Example: Tom Brady.
        limit (Union[Unset, int]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SearchV2Response]]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SearchV2Response]]:
    """General Search (v2)

     Search for sports content including teams, athletes, articles and more (legacy v2 endpoint)

    Args:
        query (str):  Example: Tom Brady.
        limit (Union[Unset, int]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SearchV2Response]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
        )
    ).parsed
