import pytest

from ensembledata.api import (
    AioHttpClient,
    EDAsyncClient,
    EDClient,
    EDError,
    HttpxAsyncClient,
    HttpxClient,
    RequestsClient,
    UrllibClient,
    errors,
)


def test_requests_client():
    client = EDClient("xxx", http_client=RequestsClient())

    with pytest.raises(EDError) as e:
        client.tiktok.user_info_from_username(username="charlidamelio")

    client.close()
    assert e.value.status_code == errors.STATUS_491_INVALID_TOKEN


def test_urllib_client():
    client = EDClient("xxx", http_client=UrllibClient())

    with pytest.raises(EDError) as e:
        client.tiktok.user_info_from_username(username="charlidamelio")

    client.close()
    assert e.value.status_code == errors.STATUS_491_INVALID_TOKEN


def test_httpx_client():
    client = EDClient("xxx", http_client=HttpxClient())

    with pytest.raises(EDError) as e:
        client.tiktok.user_info_from_username(username="charlidamelio")

    client.close()
    assert e.value.status_code == errors.STATUS_491_INVALID_TOKEN


@pytest.mark.asyncio
async def test_async_httpx_client():
    client = EDAsyncClient("xxx", http_client=HttpxAsyncClient())

    with pytest.raises(EDError) as e:
        await client.tiktok.user_info_from_username(username="charlidamelio")

    await client.close()
    assert e.value.status_code == errors.STATUS_491_INVALID_TOKEN


@pytest.mark.asyncio
async def test_aiohttp_client():
    client = EDAsyncClient("xxx", http_client=AioHttpClient())

    with pytest.raises(EDError) as e:
        await client.tiktok.user_info_from_username(username="charlidamelio")

    await client.close()
    assert e.value.status_code == errors.STATUS_491_INVALID_TOKEN
