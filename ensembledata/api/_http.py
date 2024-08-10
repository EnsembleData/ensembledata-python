from __future__ import annotations

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


class HttpClient(Protocol):
    def get(self, url: str, params: Mapping[str, Any]) -> tuple[int, Any, Mapping[str, Any]]: ...

    def close(self): ...


class AsyncHttpClient(Protocol):
    async def get(
        self, url: str, params: Mapping[str, Any]
    ) -> tuple[int, Any, Mapping[str, Any]]: ...

    async def close(self): ...


DEFAULT_TIMEOUT = 600


def default_async_client(timeout: int = DEFAULT_TIMEOUT):
    if httpx:
        print("HttpxAsyncClient")
        return HttpxAsyncClient(timeout=timeout)
    if aiohttp:
        print("AioHttpClient")
        return AioHttpClient(timeout=timeout)

    raise ImportError(
        "No async HTTP client available. To use async please make sure to install"
        " either httpx or aiohttp. Alternatively, you can implement your own version of the"
        " AsyncHttpClient protocol."
    )


def default_sync_client(timeout: int = DEFAULT_TIMEOUT):
    if httpx:
        print("HttpxClient")
        return HttpxClient(timeout=timeout)
    if requests:
        print("RequestsClient")
        return RequestsClient(timeout=timeout)

    print("UrllibClient")
    return UrllibClient()


class UrllibClient(HttpClient):
    def __init__(self, timeout: int = DEFAULT_TIMEOUT):
        self._timeout = timeout

    def get(self, url: str, params: Mapping[str, Any]):
        url += "?" + urllib.parse.urlencode(params, doseq=True, safe="/")
        req = urllib.request.Request(url, method="GET", headers={})

        try:
            with urllib.request.urlopen(req, timeout=self._timeout) as res:
                return res.status, json.loads(res.read().decode()), dict(res.headers)
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode()), dict(e.headers)

    def close(self):
        pass


class RequestsClient(HttpClient):
    def __init__(self, timeout: int = DEFAULT_TIMEOUT):
        if not requests:
            raise ImportError("requests is not installed")
        self._session = requests.Session()
        self._timeout = timeout

    def get(self, url: str, params: Mapping[str, Any]):
        assert requests is not None
        res = self._session.get(url, params=params, timeout=self._timeout)
        return res.status_code, res.json(), res.headers

    def close(self):
        self._session.close()


class HttpxClient(HttpClient):
    def __init__(self, timeout: int = DEFAULT_TIMEOUT):
        if not httpx:
            raise ImportError("httpx is not installed")
        self._client = httpx.Client(timeout=timeout)

    def get(self, url: str, params: Mapping[str, Any]):
        res = self._client.get(url, params=params)
        return res.status_code, res.json(), res.headers

    def close(self):
        self._client.close()


class HttpxAsyncClient(AsyncHttpClient):
    def __init__(self, timeout: int = DEFAULT_TIMEOUT):
        if not httpx:
            raise ImportError("httpx is not installed")
        self._client = httpx.AsyncClient(timeout=timeout)

    async def get(self, url: str, params: Mapping[str, Any]):
        print("get httpx")
        res = await self._client.get(url, params=params)
        return res.status_code, res.json(), res.headers

    async def close(self):
        await self._client.aclose()


class AioHttpClient(AsyncHttpClient):
    def __init__(self, timeout: int = DEFAULT_TIMEOUT):
        if not aiohttp:
            raise ImportError("aiohttp is not installed")
        self._client = aiohttp.ClientSession(read_timeout=timeout)

    async def get(self, url: str, params: Mapping[str, Any]):
        print("get aiohttp")
        async with self._client.get(url, params=params) as response:
            return response.status, await response.json(), response.headers

    async def close(self):
        await self._client.close()


if __name__ == "__main__":
    client = UrllibClient()
    status, data, headers = client.get(
        "https://ensembledata.com/apis/customer/get-used-units",
        {"token": "xxx", "date": "2024-01-01"},
    )
    print(status, data, headers)
