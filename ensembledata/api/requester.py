from enum import IntEnum
from warnings import warn

import httpx

from .response import EDDataResponse, EDErrorResponse

BASE_URL = "https://ensembledata.com/apis"


class EDErrorCode(IntEnum):
    TOKEN_NOT_FOUND = 491


def _handle_response(res: httpx.Response):
    units_charged = res.headers.get("units_charged", 0)
    payload = res.json()
    assert isinstance(payload, dict)

    # In most cases there will only be a "data" field in the response if the status code is 2xx,
    # however, there are currently a few edge cases where "data" is also present in the response
    # for a 4xx status code. Thus, we'll use the presence of "data" as the indicator of a
    # successful, or rather a `data`, response.
    if "data" in payload:
        return EDDataResponse(res.status_code, payload.get("data"), units_charged)

    return EDErrorResponse(res.status_code, payload.get("detail"), units_charged)


def _check_token(token: str):
    if not isinstance(token, str) or token == "":
        warn(
            "It looks like you haven't supplied a real API token. Sign up at "
            "https://dashboard.ensembledata.com/register to get your API token",
            stacklevel=2,
        )


class Requester:
    def __init__(self, token: str):
        _check_token(token)
        self.token = token

    def get(self, url: str, params: dict):
        res = httpx.get(f"{BASE_URL}{url}", params={"token": self.token, **params})
        return _handle_response(res)


class AsyncRequester:
    def __init__(self, token: str):
        _check_token(token)
        self.token = token

    async def get(self, url: str, params: dict):
        async with httpx.AsyncClient() as client:
            res = await client.get(
                f"{BASE_URL}{url}",
                params={"token": self.token, **params},
            )
        return _handle_response(res)
