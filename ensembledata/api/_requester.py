from __future__ import annotations

import sys
from enum import IntEnum
from typing import Any
from warnings import warn

if sys.version_info >= (3, 8):
    from importlib.metadata import version

    VERSION = version("ensembledata")
else:
    VERSION = "unknown"

import httpx

from .errors import EDError
from ._response import EDResponse

BASE_URL = "https://ensembledata.com/apis"

VERSION_HEADER = "edpy-version"


class EDErrorCode(IntEnum):
    TOKEN_NOT_FOUND = 491


def _handle_response(res: httpx.Response, *, return_top_level_data: bool) -> EDResponse:
    units_charged = res.headers.get("units_charged", 0)
    payload = res.json()
    assert isinstance(payload, dict)

    # In most cases there will only be a "data" field in the response if the status code is 2xx,
    # however, there are currently a few edge cases where "data" is also present in the response
    # for a 4xx status code. Thus, we'll use the presence of "data" as the indicator of a
    # successful, or rather a `data`, response.
    if "data" in payload:
        # There are a couple of endpoints that don't use a single top level "data" field, but
        # rather have multiple top level fields, for example "nextCursor".
        if return_top_level_data:
            return EDResponse(res.status_code, payload, units_charged)

        return EDResponse(res.status_code, payload.get("data"), units_charged)

    raise EDError(res.status_code, payload.get("detail"), units_charged)


def _check_token(token: str) -> None:
    if not isinstance(token, str) or token == "":
        warn(
            "It looks like you haven't supplied a real API token. Sign up at "
            "https://dashboard.ensembledata.com/register to get your API token",
            stacklevel=2,
        )


class Requester:
    def __init__(self, token: str, *, timeout: int, max_network_retries: int):
        _check_token(token)
        self.token = token
        self.timeout = timeout
        self.max_network_retries = max_network_retries

    def get(
        self, url: str, params: dict[str, Any], *, return_top_level_data: bool = False
    ) -> EDResponse:
        for attempt in range(self.max_network_retries):
            try:
                res = httpx.get(
                    f"{BASE_URL}{url}",
                    params={"token": self.token, **params},
                    timeout=self.timeout,
                    headers={"User-Agent": f"ensembledata-python-{VERSION}"},
                )
                return _handle_response(res, return_top_level_data=return_top_level_data)
            except httpx.RequestError as e:  # noqa: PERF203
                if attempt == self.max_network_retries - 1:
                    raise e
        raise AssertionError("unreachable")


class AsyncRequester:
    def __init__(self, token: str, *, timeout: int, max_network_retries: int):
        _check_token(token)
        self.token = token
        self.timeout = timeout
        self.max_network_retries = max_network_retries

    async def get(
        self, url: str, params: dict[str, Any], return_top_level_data: bool = False
    ) -> EDResponse:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            for attempt in range(self.max_network_retries):
                try:
                    res = await client.get(
                        f"{BASE_URL}{url}",
                        params={"token": self.token, **params},
                        headers={"User-Agent": f"ensembledata-python-{VERSION}"},
                    )
                    return _handle_response(res, return_top_level_data=return_top_level_data)
                except httpx.RequestError as e:  # noqa: PERF203
                    if attempt == self.max_network_retries - 1:
                        raise e
        raise AssertionError("unreachable")
