from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.mlb_athlete_details_response import MlbAthleteDetailsResponse
from ...types import Response


def _get_kwargs(
    athlete_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/baseball/leagues/mlb/athletes/{athlete_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, MlbAthleteDetailsResponse]]:
    if response.status_code == 200:
        response_200 = MlbAthleteDetailsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, MlbAthleteDetailsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, MlbAthleteDetailsResponse]]:
    """Get MLB Athlete Details

     Retrieve detailed information for a specific MLB athlete

    Args:
        athlete_id (str):  Example: 33192.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MlbAthleteDetailsResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, MlbAthleteDetailsResponse]]:
    """Get MLB Athlete Details

     Retrieve detailed information for a specific MLB athlete

    Args:
        athlete_id (str):  Example: 33192.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, MlbAthleteDetailsResponse]
    """

    return sync_detailed(
        athlete_id=athlete_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, MlbAthleteDetailsResponse]]:
    """Get MLB Athlete Details

     Retrieve detailed information for a specific MLB athlete

    Args:
        athlete_id (str):  Example: 33192.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MlbAthleteDetailsResponse]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    athlete_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, MlbAthleteDetailsResponse]]:
    """Get MLB Athlete Details

     Retrieve detailed information for a specific MLB athlete

    Args:
        athlete_id (str):  Example: 33192.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, MlbAthleteDetailsResponse]
    """

    return (
        await asyncio_detailed(
            athlete_id=athlete_id,
            client=client,
        )
    ).parsed
