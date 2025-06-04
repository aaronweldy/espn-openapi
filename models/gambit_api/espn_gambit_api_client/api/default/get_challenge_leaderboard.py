from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_challenge_leaderboard_view import GetChallengeLeaderboardView
from ...models.leaderboard_response import LeaderboardResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    challenge_name: str,
    *,
    view: Union[Unset, GetChallengeLeaderboardView] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_view: Union[Unset, str] = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/apis/v1/challenges/{challenge_name}/leaderboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, LeaderboardResponse]]:
    if response.status_code == 200:
        response_200 = LeaderboardResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, LeaderboardResponse]]:
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
    view: Union[Unset, GetChallengeLeaderboardView] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, LeaderboardResponse]]:
    """Get Challenge Leaderboard

     Retrieve the leaderboard for a specific Pick'em challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        view (Union[Unset, GetChallengeLeaderboardView]):  Example: ranks.
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LeaderboardResponse]]
    """

    kwargs = _get_kwargs(
        challenge_name=challenge_name,
        view=view,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    challenge_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetChallengeLeaderboardView] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, LeaderboardResponse]]:
    """Get Challenge Leaderboard

     Retrieve the leaderboard for a specific Pick'em challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        view (Union[Unset, GetChallengeLeaderboardView]):  Example: ranks.
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LeaderboardResponse]
    """

    return sync_detailed(
        challenge_name=challenge_name,
        client=client,
        view=view,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    challenge_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetChallengeLeaderboardView] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, LeaderboardResponse]]:
    """Get Challenge Leaderboard

     Retrieve the leaderboard for a specific Pick'em challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        view (Union[Unset, GetChallengeLeaderboardView]):  Example: ranks.
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LeaderboardResponse]]
    """

    kwargs = _get_kwargs(
        challenge_name=challenge_name,
        view=view,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    challenge_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    view: Union[Unset, GetChallengeLeaderboardView] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, LeaderboardResponse]]:
    """Get Challenge Leaderboard

     Retrieve the leaderboard for a specific Pick'em challenge

    Args:
        challenge_name (str):  Example: nfl-pigskin-pickem-2025.
        view (Union[Unset, GetChallengeLeaderboardView]):  Example: ranks.
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LeaderboardResponse]
    """

    return (
        await asyncio_detailed(
            challenge_name=challenge_name,
            client=client,
            view=view,
            limit=limit,
            offset=offset,
        )
    ).parsed
