from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.flex_response import FlexResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region: Union[Unset, str] = "us",
    lang: Union[Unset, str] = "en",
    contentorigin: Union[Unset, str] = "espn",
    contributor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    pubkey: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["region"] = region

    params["lang"] = lang

    params["contentorigin"] = contentorigin

    params["contributor"] = contributor

    params["limit"] = limit

    params["pubkey"] = pubkey

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/apis/v2/flex",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FlexResponse]]:
    if response.status_code == 200:
        response_200 = FlexResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, FlexResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, str] = "us",
    lang: Union[Unset, str] = "en",
    contentorigin: Union[Unset, str] = "espn",
    contributor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    pubkey: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FlexResponse]]:
    """Get Contributor Posts

     Retrieve contributor posts and content in a flexible layout format

    Args:
        region (Union[Unset, str]):  Default: 'us'.
        lang (Union[Unset, str]):  Default: 'en'.
        contentorigin (Union[Unset, str]):  Default: 'espn'.
        contributor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        pubkey (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FlexResponse]]
    """

    kwargs = _get_kwargs(
        region=region,
        lang=lang,
        contentorigin=contentorigin,
        contributor=contributor,
        limit=limit,
        pubkey=pubkey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, str] = "us",
    lang: Union[Unset, str] = "en",
    contentorigin: Union[Unset, str] = "espn",
    contributor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    pubkey: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FlexResponse]]:
    """Get Contributor Posts

     Retrieve contributor posts and content in a flexible layout format

    Args:
        region (Union[Unset, str]):  Default: 'us'.
        lang (Union[Unset, str]):  Default: 'en'.
        contentorigin (Union[Unset, str]):  Default: 'espn'.
        contributor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        pubkey (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FlexResponse]
    """

    return sync_detailed(
        client=client,
        region=region,
        lang=lang,
        contentorigin=contentorigin,
        contributor=contributor,
        limit=limit,
        pubkey=pubkey,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, str] = "us",
    lang: Union[Unset, str] = "en",
    contentorigin: Union[Unset, str] = "espn",
    contributor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    pubkey: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FlexResponse]]:
    """Get Contributor Posts

     Retrieve contributor posts and content in a flexible layout format

    Args:
        region (Union[Unset, str]):  Default: 'us'.
        lang (Union[Unset, str]):  Default: 'en'.
        contentorigin (Union[Unset, str]):  Default: 'espn'.
        contributor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        pubkey (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FlexResponse]]
    """

    kwargs = _get_kwargs(
        region=region,
        lang=lang,
        contentorigin=contentorigin,
        contributor=contributor,
        limit=limit,
        pubkey=pubkey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, str] = "us",
    lang: Union[Unset, str] = "en",
    contentorigin: Union[Unset, str] = "espn",
    contributor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    pubkey: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FlexResponse]]:
    """Get Contributor Posts

     Retrieve contributor posts and content in a flexible layout format

    Args:
        region (Union[Unset, str]):  Default: 'us'.
        lang (Union[Unset, str]):  Default: 'en'.
        contentorigin (Union[Unset, str]):  Default: 'espn'.
        contributor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        pubkey (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FlexResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            lang=lang,
            contentorigin=contentorigin,
            contributor=contributor,
            limit=limit,
            pubkey=pubkey,
        )
    ).parsed
