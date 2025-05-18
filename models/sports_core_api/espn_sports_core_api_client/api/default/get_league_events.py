from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.league_enum import LeagueEnum
from ...models.paginated_reference_list_response import PaginatedReferenceListResponse
from ...models.sport_enum import SportEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    week: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    seasontypes: Union[Unset, str] = UNSET,
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["week"] = week

    params["season"] = season

    params["seasontypes"] = seasontypes

    params["lang"] = lang

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/{sport}/leagues/{league}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedReferenceListResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    week: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    seasontypes: Union[Unset, str] = UNSET,
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get League Events

     Retrieve the list of events for a given league and sport. Returns a paginated list of event resource
    references.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        week (Union[Unset, int]):  Example: 1.
        season (Union[Unset, int]):  Example: 2024.
        seasontypes (Union[Unset, str]):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedReferenceListResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        week=week,
        season=season,
        seasontypes=seasontypes,
        lang=lang,
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    week: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    seasontypes: Union[Unset, str] = UNSET,
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get League Events

     Retrieve the list of events for a given league and sport. Returns a paginated list of event resource
    references.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        week (Union[Unset, int]):  Example: 1.
        season (Union[Unset, int]):  Example: 2024.
        seasontypes (Union[Unset, str]):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedReferenceListResponse]
    """

    return sync_detailed(
        sport=sport,
        league=league,
        client=client,
        week=week,
        season=season,
        seasontypes=seasontypes,
        lang=lang,
        region=region,
    ).parsed


async def asyncio_detailed(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    week: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    seasontypes: Union[Unset, str] = UNSET,
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get League Events

     Retrieve the list of events for a given league and sport. Returns a paginated list of event resource
    references.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        week (Union[Unset, int]):  Example: 1.
        season (Union[Unset, int]):  Example: 2024.
        seasontypes (Union[Unset, str]):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedReferenceListResponse]]
    """

    kwargs = _get_kwargs(
        sport=sport,
        league=league,
        week=week,
        season=season,
        seasontypes=seasontypes,
        lang=lang,
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sport: SportEnum,
    league: LeagueEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    week: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    seasontypes: Union[Unset, str] = UNSET,
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get League Events

     Retrieve the list of events for a given league and sport. Returns a paginated list of event resource
    references.

    Args:
        sport (SportEnum): Common sport identifiers used in ESPN APIs.
        league (LeagueEnum): Common league identifiers used in ESPN APIs.
        week (Union[Unset, int]):  Example: 1.
        season (Union[Unset, int]):  Example: 2024.
        seasontypes (Union[Unset, str]):  Example: 2.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedReferenceListResponse]
    """

    return (
        await asyncio_detailed(
            sport=sport,
            league=league,
            client=client,
            week=week,
            season=season,
            seasontypes=seasontypes,
            lang=lang,
            region=region,
        )
    ).parsed
