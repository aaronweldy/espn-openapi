from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_list_response import CalendarListResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    sport: str,
    league: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/calendar",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CalendarListResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CalendarListResponse.from_dict(response.json())

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
) -> Response[Union[CalendarListResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: str,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CalendarListResponse, ErrorResponse]]:
    """Get League Calendar

     Retrieve the calendar for a given league and sport (e.g., NFL, NBA, etc). Returns a list of calendar
    resource references.

    Args:
        sport (str):  Example: football.
        league (str):  Example: nfl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarListResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: str,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CalendarListResponse, ErrorResponse]]:
    """Get League Calendar

     Retrieve the calendar for a given league and sport (e.g., NFL, NBA, etc). Returns a list of calendar
    resource references.

    Args:
        sport (str):  Example: football.
        league (str):  Example: nfl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarListResponse, ErrorResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
    ).parsed


async def asyncio_detailed(
    sport: str,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CalendarListResponse, ErrorResponse]]:
    """Get League Calendar

     Retrieve the calendar for a given league and sport (e.g., NFL, NBA, etc). Returns a list of calendar
    resource references.

    Args:
        sport (str):  Example: football.
        league (str):  Example: nfl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarListResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: str,
    league: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CalendarListResponse, ErrorResponse]]:
    """Get League Calendar

     Retrieve the calendar for a given league and sport (e.g., NFL, NBA, etc). Returns a list of calendar
    resource references.

    Args:
        sport (str):  Example: football.
        league (str):  Example: nfl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarListResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
        )
    ).parsed
