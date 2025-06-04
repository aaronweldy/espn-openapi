from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_response import ChallengeResponse
from ...models.error_response import ErrorResponse
from ...models.get_challenge_details_view import GetChallengeDetailsView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    challenge_name: str,
    *,
    scoring_period_id: Union[Unset, int] = UNSET,
    view: Union[Unset, GetChallengeDetailsView] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["scoringPeriodId"] = scoring_period_id

    json_view: Union[Unset, str] = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v1/challenges/{challenge_name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChallengeResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = ChallengeResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ChallengeResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    challenge_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
    view: Union[Unset, GetChallengeDetailsView] = UNSET,
) -> Response[Union[ChallengeResponse, ErrorResponse]]:
    """Get Challenge Details

     Retrieve detailed information about a specific Pick'em challenge.
    Common challenge names include 'nfl-pigskin-pickem-2025' for NFL Pick'em.

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        scoring_period_id (Union[Unset, int]):  Example: 1.
        view (Union[Unset, GetChallengeDetailsView]):  Example: picks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        challenge_name=challenge_name,
        scoring_period_id=scoring_period_id,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    challenge_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
    view: Union[Unset, GetChallengeDetailsView] = UNSET,
) -> Optional[Union[ChallengeResponse, ErrorResponse]]:
    """Get Challenge Details

     Retrieve detailed information about a specific Pick'em challenge.
    Common challenge names include 'nfl-pigskin-pickem-2025' for NFL Pick'em.

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        scoring_period_id (Union[Unset, int]):  Example: 1.
        view (Union[Unset, GetChallengeDetailsView]):  Example: picks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeResponse, ErrorResponse]
    """

    return sync_detailed(
        challenge_name=challenge_name,
        client=client,
        scoring_period_id=scoring_period_id,
        view=view,
    ).parsed


async def asyncio_detailed(
    challenge_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
    view: Union[Unset, GetChallengeDetailsView] = UNSET,
) -> Response[Union[ChallengeResponse, ErrorResponse]]:
    """Get Challenge Details

     Retrieve detailed information about a specific Pick'em challenge.
    Common challenge names include 'nfl-pigskin-pickem-2025' for NFL Pick'em.

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        scoring_period_id (Union[Unset, int]):  Example: 1.
        view (Union[Unset, GetChallengeDetailsView]):  Example: picks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        challenge_name=challenge_name,
        scoring_period_id=scoring_period_id,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    challenge_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scoring_period_id: Union[Unset, int] = UNSET,
    view: Union[Unset, GetChallengeDetailsView] = UNSET,
) -> Optional[Union[ChallengeResponse, ErrorResponse]]:
    """Get Challenge Details

     Retrieve detailed information about a specific Pick'em challenge.
    Common challenge names include 'nfl-pigskin-pickem-2025' for NFL Pick'em.

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        scoring_period_id (Union[Unset, int]):  Example: 1.
        view (Union[Unset, GetChallengeDetailsView]):  Example: picks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            challenge_name=challenge_name,
            client=client,
            scoring_period_id=scoring_period_id,
            view=view,
        )
    ).parsed
