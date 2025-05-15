from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athlete_overview_response import AthleteOverviewResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    athlete_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/common/v3/sports/football/nfl/athletes/{athlete_id}/overview",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AthleteOverviewResponse, Error]]:
    if response.status_code == 200:
        response_200 = AthleteOverviewResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AthleteOverviewResponse, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteOverviewResponse, Error]]:
    """Get NFL athlete overview

    Args:
        athlete_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteOverviewResponse, Error]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteOverviewResponse, Error]]:
    """Get NFL athlete overview

    Args:
        athlete_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteOverviewResponse, Error]
    """

    return sync_detailed(
        athlete_id=athlete_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AthleteOverviewResponse, Error]]:
    """Get NFL athlete overview

    Args:
        athlete_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AthleteOverviewResponse, Error]]
    """

    kwargs = _get_kwargs(
        athlete_id=athlete_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    athlete_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AthleteOverviewResponse, Error]]:
    """Get NFL athlete overview

    Args:
        athlete_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AthleteOverviewResponse, Error]
    """

    return (
        await asyncio_detailed(
            athlete_id=athlete_id,
            client=client,
        )
    ).parsed
