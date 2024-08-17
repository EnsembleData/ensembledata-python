from __future__ import annotations

from typing import Any, Mapping
from warnings import warn

from ._http import (
    AsyncHttpClient,
    HttpClient,
    RetryableError,
    default_async_client,
    default_sync_client,
)
from ._response import EDResponse
from ._version import version
from .errors import EDError

BASE_URL = "https://ensembledata.com/apis"
USER_AGENT = f"ensembledata-python/{version}"


def _handle_response(
    status_code: int, payload: Any, headers: Mapping[str, Any], *, return_top_level_data: bool
) -> EDResponse:
    units_charged = headers.get("units_charged", 0)
    assert isinstance(payload, dict)

    # In most cases there will only be a "data" field in the response if the status code is 2xx,
    # however, there are currently a few edge cases where "data" is also present in the response
    # for a 4xx status code. Thus, we'll use the presence of "data" as the indicator of a
    # successful, or rather a `data`, response.
    if "data" in payload:
        # There are a couple of endpoints that don't use a single top level "data" field, but
        # rather have multiple top level fields, for example "nextCursor".
        if return_top_level_data:
            return EDResponse(status_code, payload, units_charged)

        return EDResponse(status_code, payload.get("data"), units_charged)

    raise EDError(status_code, payload.get("detail"), units_charged)


def _check_token(token: str) -> None:
    if not isinstance(token, str) or token == "":
        warn(
            "It looks like you haven't supplied a real API token. Sign up at "
            "https://dashboard.ensembledata.com/register to get your API token",
            stacklevel=2,
        )


class Requester:
    def __init__(
        self,
        token: str,
        *,
        timeout: float,
        max_network_retries: int,
        http_client: HttpClient | None = None,
    ):
        _check_token(token)
        self.token = token
        self.timeout = timeout
        self.max_network_retries = max_network_retries
        self.http_client = http_client or default_sync_client(timeout=timeout)
        print(self.http_client)

    def get(
        self,
        url: str,
        params: Mapping[str, Any],
        *,
        timeout: float | None = None,
        return_top_level_data: bool = False,
    ) -> EDResponse:
        for attempt in range(self.max_network_retries):
            try:
                status_code, payload, headers = self.http_client.get(
                    f"{BASE_URL}{url}",
                    params={"token": self.token, **params},
                    timeout=timeout,
                    headers={"User-Agent": USER_AGENT},
                )
                return _handle_response(
                    status_code, payload, headers, return_top_level_data=return_top_level_data
                )
            except RetryableError as e:  # noqa: PERF203
                if attempt == self.max_network_retries - 1:
                    raise e
        raise AssertionError("unreachable")


class AsyncRequester:
    def __init__(
        self,
        token: str,
        *,
        timeout: float,
        max_network_retries: int,
        http_client: AsyncHttpClient | None = None,
    ):
        _check_token(token)
        self.token = token
        self.timeout = timeout
        self.max_network_retries = max_network_retries
        self.http_client = http_client or default_async_client(timeout=timeout)

    async def get(
        self,
        url: str,
        params: Mapping[str, Any],
        *,
        timeout: float | None = None,
        return_top_level_data: bool = False,
    ) -> EDResponse:
        for attempt in range(self.max_network_retries):
            try:
                res = await self.http_client.get(
                    f"{BASE_URL}{url}",
                    params={"token": self.token, **params},
                    headers={"User-Agent": USER_AGENT},
                    timeout=timeout,
                )
                return _handle_response(*res, return_top_level_data=return_top_level_data)
            except RetryableError as e:  # noqa: PERF203
                if attempt == self.max_network_retries - 1:
                    raise e
        raise AssertionError("unreachable")
