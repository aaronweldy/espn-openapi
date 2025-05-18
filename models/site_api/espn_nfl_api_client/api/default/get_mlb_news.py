from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.sport_news_api_schema import SportNewsAPISchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["team"] = team

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sports/baseball/mlb/news",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SportNewsAPISchema]]:
    if response.status_code == 200:
        response_200 = SportNewsAPISchema.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SportNewsAPISchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get MLB News

     Retrieve the latest MLB news articles and headlines

    Args:
        limit (Union[Unset, int]):  Example: 10.
        offset (Union[Unset, int]):
        team (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SportNewsAPISchema]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        team=team,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get MLB News

     Retrieve the latest MLB news articles and headlines

    Args:
        limit (Union[Unset, int]):  Example: 10.
        offset (Union[Unset, int]):
        team (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SportNewsAPISchema]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        team=team,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get MLB News

     Retrieve the latest MLB news articles and headlines

    Args:
        limit (Union[Unset, int]):  Example: 10.
        offset (Union[Unset, int]):
        team (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SportNewsAPISchema]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        team=team,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    team: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SportNewsAPISchema]]:
    """Get MLB News

     Retrieve the latest MLB news articles and headlines

    Args:
        limit (Union[Unset, int]):  Example: 10.
        offset (Union[Unset, int]):
        team (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SportNewsAPISchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            team=team,
        )
    ).parsed
