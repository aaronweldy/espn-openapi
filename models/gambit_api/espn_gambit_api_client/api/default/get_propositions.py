from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.proposition import Proposition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    challenge_id: int,
    view: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["challengeId"] = challenge_id

    params["view"] = view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apis/v1/propositions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, list["Proposition"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Proposition.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[ErrorResponse, list["Proposition"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    challenge_id: int,
    view: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, list["Proposition"]]]:
    """Get Propositions

     Retrieve propositions (picks) for a challenge.
    Note: the live API returns a top-level JSON array of proposition objects,
    not an envelope object. Use the numeric challenge ID returned by
    `/apis/v1/challenges/{challengeName}`.

    Args:
        challenge_id (int):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, list['Proposition']]]
    """

    kwargs = _get_kwargs(
        challenge_id=challenge_id,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    challenge_id: int,
    view: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, list["Proposition"]]]:
    """Get Propositions

     Retrieve propositions (picks) for a challenge.
    Note: the live API returns a top-level JSON array of proposition objects,
    not an envelope object. Use the numeric challenge ID returned by
    `/apis/v1/challenges/{challengeName}`.

    Args:
        challenge_id (int):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, list['Proposition']]
    """

    return sync_detailed(
        client=client,
        challenge_id=challenge_id,
        view=view,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    challenge_id: int,
    view: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, list["Proposition"]]]:
    """Get Propositions

     Retrieve propositions (picks) for a challenge.
    Note: the live API returns a top-level JSON array of proposition objects,
    not an envelope object. Use the numeric challenge ID returned by
    `/apis/v1/challenges/{challengeName}`.

    Args:
        challenge_id (int):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, list['Proposition']]]
    """

    kwargs = _get_kwargs(
        challenge_id=challenge_id,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    challenge_id: int,
    view: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, list["Proposition"]]]:
    """Get Propositions

     Retrieve propositions (picks) for a challenge.
    Note: the live API returns a top-level JSON array of proposition objects,
    not an envelope object. Use the numeric challenge ID returned by
    `/apis/v1/challenges/{challengeName}`.

    Args:
        challenge_id (int):
        view (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, list['Proposition']]
    """

    return (
        await asyncio_detailed(
            client=client,
            challenge_id=challenge_id,
            view=view,
        )
    ).parsed
