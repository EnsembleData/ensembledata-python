import pytest

from ensembledata.api import EDAsyncClient, EDClient, EDError, errors


def test_client():
    client = EDClient("xxx")

    with pytest.raises(EDError) as e:
        client.customer.get_usage("2024-01-01")

    assert e.value.status_code == errors.STATUS_491_INVALID_TOKEN


@pytest.mark.asyncio
async def test_async_client():
    client = EDAsyncClient("xxx")

    with pytest.raises(EDError) as e:
        await client.customer.get_usage("2024-01-01")

    assert e.value.status_code == errors.STATUS_491_INVALID_TOKEN
