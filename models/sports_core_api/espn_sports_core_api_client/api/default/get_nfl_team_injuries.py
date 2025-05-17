from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.paginated_reference_list_response import PaginatedReferenceListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageIndex"] = page_index

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sports/football/leagues/nfl/teams/{team_id}/injuries",
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
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get NFL Team Injuries

     Retrieve a paginated list of injury references for a specific NFL team.

    Args:
        team_id (str):  Example: 12.
        page_index (Union[Unset, int]):  Example: 1.
        page_size (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedReferenceListResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        page_index=page_index,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get NFL Team Injuries

     Retrieve a paginated list of injury references for a specific NFL team.

    Args:
        team_id (str):  Example: 12.
        page_index (Union[Unset, int]):  Example: 1.
        page_size (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedReferenceListResponse]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        page_index=page_index,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get NFL Team Injuries

     Retrieve a paginated list of injury references for a specific NFL team.

    Args:
        team_id (str):  Example: 12.
        page_index (Union[Unset, int]):  Example: 1.
        page_size (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedReferenceListResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        page_index=page_index,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PaginatedReferenceListResponse]]:
    """Get NFL Team Injuries

     Retrieve a paginated list of injury references for a specific NFL team.

    Args:
        team_id (str):  Example: 12.
        page_index (Union[Unset, int]):  Example: 1.
        page_size (Union[Unset, int]):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedReferenceListResponse]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            page_index=page_index,
            page_size=page_size,
        )
    ).parsed
