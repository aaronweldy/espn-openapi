from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nfl_standings_response import NflStandingsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    season: Union[Unset, int] = UNSET,
    xhr: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["season"] = season

    params["xhr"] = xhr

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/core/nfl/standings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NflStandingsResponse]:
    if response.status_code == 200:
        response_200 = NflStandingsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NflStandingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    xhr: Union[Unset, int] = UNSET,
) -> Response[NflStandingsResponse]:
    """NFL Standings

     Get the NFL standings data.

    Args:
        season (Union[Unset, int]):
        xhr (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflStandingsResponse]
    """

    kwargs = _get_kwargs(
        season=season,
        xhr=xhr,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    xhr: Union[Unset, int] = UNSET,
) -> Optional[NflStandingsResponse]:
    """NFL Standings

     Get the NFL standings data.

    Args:
        season (Union[Unset, int]):
        xhr (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflStandingsResponse
    """

    return sync_detailed(
        client=client,
        season=season,
        xhr=xhr,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    xhr: Union[Unset, int] = UNSET,
) -> Response[NflStandingsResponse]:
    """NFL Standings

     Get the NFL standings data.

    Args:
        season (Union[Unset, int]):
        xhr (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NflStandingsResponse]
    """

    kwargs = _get_kwargs(
        season=season,
        xhr=xhr,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, int] = UNSET,
    xhr: Union[Unset, int] = UNSET,
) -> Optional[NflStandingsResponse]:
    """NFL Standings

     Get the NFL standings data.

    Args:
        season (Union[Unset, int]):
        xhr (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NflStandingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            season=season,
            xhr=xhr,
        )
    ).parsed
