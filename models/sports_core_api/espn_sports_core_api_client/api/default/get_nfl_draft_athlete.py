from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.nfl_draft_athlete_response import NflDraftAthleteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    athlete_id: str,
    *,
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["lang"] = lang

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/football/leagues/nfl/seasons/{year}/draft/athletes/{athlete_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NflDraftAthleteResponse]]:
    if response.status_code == 200:
        response_200 = NflDraftAthleteResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NflDraftAthleteResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, NflDraftAthleteResponse]]:
    """Get NFL Draft Athlete Details

     Retrieve details for a specific NFL draft athlete (core API).

    Args:
        year (int):  Example: 2023.
        athlete_id (str):  Example: 106308.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NflDraftAthleteResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        athlete_id=athlete_id,
        lang=lang,
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, NflDraftAthleteResponse]]:
    """Get NFL Draft Athlete Details

     Retrieve details for a specific NFL draft athlete (core API).

    Args:
        year (int):  Example: 2023.
        athlete_id (str):  Example: 106308.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NflDraftAthleteResponse]
    """

    return sync_detailed(
        year=year,
        athlete_id=athlete_id,
        client=client,
        lang=lang,
        region=region,
    ).parsed


async def asyncio_detailed(
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, NflDraftAthleteResponse]]:
    """Get NFL Draft Athlete Details

     Retrieve details for a specific NFL draft athlete (core API).

    Args:
        year (int):  Example: 2023.
        athlete_id (str):  Example: 106308.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NflDraftAthleteResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        athlete_id=athlete_id,
        lang=lang,
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    lang: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, NflDraftAthleteResponse]]:
    """Get NFL Draft Athlete Details

     Retrieve details for a specific NFL draft athlete (core API).

    Args:
        year (int):  Example: 2023.
        athlete_id (str):  Example: 106308.
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NflDraftAthleteResponse]
    """

    return (
        await asyncio_detailed(
            year=year,
            athlete_id=athlete_id,
            client=client,
            lang=lang,
            region=region,
        )
    ).parsed
