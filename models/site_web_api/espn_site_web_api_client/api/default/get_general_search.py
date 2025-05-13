from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_general_search_mode import GetGeneralSearchMode
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, GetGeneralSearchMode] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query"] = query

    params["limit"] = limit

    json_mode: Union[Unset, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/apis/common/v3/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SearchResponse]]:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SearchResponse]]:
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
    mode: Union[Unset, GetGeneralSearchMode] = UNSET,
) -> Response[Union[ErrorResponse, SearchResponse]]:
    """General Search

     Search for sports content including teams, athletes, articles and more

    Args:
        query (str):  Example: Mahomes.
        limit (Union[Unset, int]):  Example: 10.
        mode (Union[Unset, GetGeneralSearchMode]):  Example: prefix.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SearchResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        mode=mode,
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
    mode: Union[Unset, GetGeneralSearchMode] = UNSET,
) -> Optional[Union[ErrorResponse, SearchResponse]]:
    """General Search

     Search for sports content including teams, athletes, articles and more

    Args:
        query (str):  Example: Mahomes.
        limit (Union[Unset, int]):  Example: 10.
        mode (Union[Unset, GetGeneralSearchMode]):  Example: prefix.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SearchResponse]
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, GetGeneralSearchMode] = UNSET,
) -> Response[Union[ErrorResponse, SearchResponse]]:
    """General Search

     Search for sports content including teams, athletes, articles and more

    Args:
        query (str):  Example: Mahomes.
        limit (Union[Unset, int]):  Example: 10.
        mode (Union[Unset, GetGeneralSearchMode]):  Example: prefix.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SearchResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, GetGeneralSearchMode] = UNSET,
) -> Optional[Union[ErrorResponse, SearchResponse]]:
    """General Search

     Search for sports content including teams, athletes, articles and more

    Args:
        query (str):  Example: Mahomes.
        limit (Union[Unset, int]):  Example: 10.
        mode (Union[Unset, GetGeneralSearchMode]):  Example: prefix.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SearchResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
            mode=mode,
        )
    ).parsed
