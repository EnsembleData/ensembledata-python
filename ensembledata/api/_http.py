from __future__ import annotations

import socket
import sys
from typing import Any, Mapping

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

try:
    import requests
except ImportError:
    requests = None

try:
    import httpx
except ImportError:
    httpx = None

try:
    import aiohttp
except ImportError:
    aiohttp = None

import json
import urllib.error
import urllib.parse
import urllib.request


class RetryableError(Exception):
    """
    An error to signify that the request can be retried.

    Implementers of the HttpClient or AsyncHttpClient protocol should raise this error to signify
    that an error occurred, however, it is reasonable to retry the request.
    """


class HttpClient(Protocol):
    def get(
        self,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout: float | None = None,
    ) -> tuple[int, Any, Mapping[str, Any]]: ...

    def close(self): ...


class AsyncHttpClient(Protocol):
    async def get(
        self,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout: float | None = None,
    ) -> tuple[int, Any, Mapping[str, Any]]: ...

    async def close(self): ...


DEFAULT_TIMEOUT = 600


def default_async_client(timeout: float = DEFAULT_TIMEOUT):
    if httpx:
        return HttpxAsyncClient(timeout=timeout)
    if aiohttp:
        return AioHttpClient(timeout=timeout)
    raise ImportError(
        "No async HTTP client available. To use async please make sure to install"
        " either `httpx` or `aiohttp`. Alternatively, you can implement your own version of the"
        " AsyncHttpClient protocol."
    )


def default_sync_client(timeout: float = DEFAULT_TIMEOUT):
    if httpx:
        return HttpxClient(timeout=timeout)
    if requests:
        return RequestsClient(timeout=timeout)
    return UrllibClient()


class UrllibClient(HttpClient):
    def __init__(self, timeout: float = DEFAULT_TIMEOUT):
        self._timeout = timeout

    def get(
        self,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout: float | None = None,
    ) -> tuple[int, Any, Mapping[str, Any]]:
        url += "?" + urllib.parse.urlencode(params, doseq=True, safe="/")
        req = urllib.request.Request(url, method="GET", headers=dict(headers))
        timeout = self._timeout if timeout is None else timeout
        try:
            with urllib.request.urlopen(req, timeout=timeout) as res:
                return res.status, json.loads(res.read().decode()), dict(res.headers)
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode()), dict(e.headers)
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                raise
            raise RetryableError from e

    def close(self):
        pass


class RequestsClient(HttpClient):
    def __init__(self, timeout: float = DEFAULT_TIMEOUT):
        if not requests:
            raise ImportError(
                "It appears `requests` is not installed. "
                "Please install it to use the RequestsClient."
            )
        self._session = requests.Session()
        self._timeout = timeout

    def get(
        self,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout: float | None = None,
    ) -> tuple[int, Any, Mapping[str, Any]]:
        assert requests is not None
        try:
            res = self._session.get(
                url,
                params=params,
                headers=headers,
                timeout=(self._timeout if timeout is None else timeout),
            )
            return res.status_code, res.json(), res.headers
        except requests.RequestException as e:
            if isinstance(e, requests.ReadTimeout):
                raise
            raise RetryableError from e

    def close(self):
        self._session.close()


class HttpxClient(HttpClient):
    def __init__(self, timeout: float = DEFAULT_TIMEOUT):
        if not httpx:
            raise ImportError(
                "It appears `httpx` is not installed. Please install it to use the HttpxClient."
            )
        self._timeout = timeout

        # We don't set the timeout on the client itself, as it is simpler to set it per request.
        # Why? A user may or may not override the timeout on a per-request basis. In the case
        # the user doesn't set a specific timeout on the request, it is slightly annoying to
        # indicate that the default client timeout should be used. You can do this by not passing
        # a timeout, but this creates some not-so-nice duplicated code with an if-else.
        self._client = httpx.Client(timeout=timeout)

    def get(
        self,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout: float | None = None,
    ) -> tuple[int, Any, Mapping[str, Any]]:
        assert httpx is not None
        timeout = self._timeout if timeout is None else timeout
        try:
            res = self._client.get(url, params=params, headers=headers, timeout=timeout)
            return res.status_code, res.json(), res.headers
        except httpx.RequestError as e:
            if isinstance(e, httpx.ReadTimeout):
                raise
            raise RetryableError from e

    def close(self):
        self._client.close()


class HttpxAsyncClient(AsyncHttpClient):
    def __init__(self, timeout: float = DEFAULT_TIMEOUT):
        if not httpx:
            raise ImportError(
                "It appears `httpx` is not installed. "
                "Please install it to use the HttpxAsyncClient."
            )
        self._timeout = timeout

        # We don't set the timeout on the client itself, as it is simpler to set it per request.
        # Why? A user may or may not override the timeout on a per-request basis. In the case
        # the user doesn't set a specific timeout on the request, it is slightly annoying to
        # indicate that the default client timeout should be used. You can do this by not passing
        # a timeout, but this creates some not-so-nice duplicated code with an if-else.
        self._client = httpx.AsyncClient()

    async def get(
        self,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout: float | None = None,
    ) -> tuple[int, Any, Mapping[str, Any]]:
        assert httpx is not None
        timeout = self._timeout if timeout is None else timeout
        try:
            res = await self._client.get(url, params=params, headers=headers, timeout=timeout)
            return res.status_code, res.json(), res.headers
        except httpx.RequestError as e:
            if isinstance(e, httpx.ReadTimeout):
                raise
            raise RetryableError from e

    async def close(self):
        await self._client.aclose()


class AioHttpClient(AsyncHttpClient):
    def __init__(self, timeout: float = DEFAULT_TIMEOUT):
        if not aiohttp:
            raise ImportError(
                "It appears `aiohttp` is not installed. "
                "Please install it to use the AioHttpClient."
            )
        self._timeout = timeout

        # We don't set the timeout on the client itself, as it is simpler to set it per request.
        # Why? A user may or may not override the timeout on a per-request basis. In the case
        # the user doesn't set a specific timeout on the request, it is slightly annoying to
        # indicate that the default client timeout should be used. You can do this by not passing
        # a timeout, but this creates some not-so-nice duplicated code with an if-else.
        self._client = aiohttp.ClientSession()

    async def get(
        self,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout: float | None = None,
    ) -> tuple[int, Any, Mapping[str, Any]]:
        assert aiohttp is not None
        timeout = self._timeout if timeout is None else timeout
        try:
            async with self._client.get(
                url,
                params=params,
                headers=headers,
                timeout=aiohttp.ClientTimeout(timeout),
            ) as response:
                return response.status, await response.json(), response.headers
        except aiohttp.ClientError as e:
            if isinstance(e, aiohttp.ServerTimeoutError):
                raise
            raise RetryableError from e

    async def close(self):
        await self._client.close()
