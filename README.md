# EnsembleData Python API

[![pypi](https://img.shields.io/pypi/v/ensembledata?color=%2334D058&label=pypi%20package)](https://pypi.org/project/ensembledata/)
[![pypi](https://img.shields.io/pypi/pyversions/ensembledata.svg)](https://pypi.org/project/ensembledata/)

## Documentation

Check out the [API docs](https://ensembledata.com/apis/docs) to see which endpoints are available for each social media and for detailed descriptions of their parameters and functionality.

## Installation

Install the package with pip as you would any other python package.

```bash
pip install ensembledata
```

It's also recommended (though not mandatory) to install `httpx` for sending requests, however, the `requests` and `aiohttp` packages can also be used. See [configuring an http client](#configure-a-http-client) for more info.

### Requirements

- Python 3.7+. 

## Usage

[Register](https://dashboard.ensembledata.com/register) to get your free API token.

```python
from ensembledata.api import EDClient


client = EDClient("API-TOKEN")
result = client.tiktok.user_info_from_username(username="daviddobrik")

print("Data: ", result.data)
print("Units charged:", result.units_charged)

# Other Examples:
# result = client.instagram.user_info(username="daviddobrik")
# result = client.youtube.channel_subscribers(channel_id="UCnQghMm3Z164JFhScQYFTBw")
```

#### TikTok Guide
Get started with the [TikTok API Guide](https://github.com/ensembledata/tiktok-scraper). Find out which endpoints are available, and how you can use them with examples using the ensembledata python package.

#### Instagram Guide
Coming soon...

<br>

### Missing Endpoints / Parameters

If you find that one of the endpoints from our [API docs](https://ensembledata.com/apis/docs) is not yet available in this package, you can use the `EDClient.request` method to specify the endpoint manually in the meantime. 

```python
from ensembledata.api import EDClient

client = EDClient("API-TOKEN")
result = client.request("/instagram/[example]", params={"foo": "...", "bar": "..."})
```

If you find that one the parameters to an existing endpoint is missing, you can still send this parameter via the `extra_params` dictionary which is available on all endpoint methods. See the example below:
```python
from ensembledata.api import EDClient

client = EDClient("API-TOKEN")
result = client.instagram.user_info(username="...", extra_params={"baz": "..."})
```

<br>

### Handling Errors

In the [API docs](https://ensembledata.com/apis/docs), each endpoint lists a handful of possible errors the API may respond with. You can handle these errors by catching the `EDError` exception. 

```python
from ensembledata.api import EDClient, EDError, errors


client = EDClient("API-TOKEN")
try:
    result = client.tiktok.user_info_from_username(username="daviddobrik")
except EDError as e:

    # Rate limit exceeded...
    if e.status_code == errors.STATUS_429_RATE_LIMIT_EXCEEDED:
        print(e.detail)

    # Subscription expired...
    if e.status_code == errors.STATUS_493_SUBSCRIPTION_EXPIRED:
        print(e.detail)

except Exception as e:
    # Some other error occurred, unrelated to the EnsembleData API
    # E.g. httpx.RequestError, json.JSONDecodeError
    pass

    
```

<br>

### Async 

This package provides an asynchronous client, `EDAsyncClient`, which will give you access to async versions of all the same methods that can be found on the `EDClient`. 

Note: you must install either `httpx` or `aiohttp` for sending async requests.

```python
import asyncio

from ensembledata.api import EDAsyncClient


async def main():
    client = EDAsyncClient("API-TOKEN")
    result = await client.tiktok.user_info_from_username(username="daviddobrik")

if __name__ == "__main__":
    asyncio.run(main())
```

<br>

### Configure a HTTP Client

This package comes with support for `httpx`, `requests`, `aiohttp` and `urllib`. If you don't have any of these installed, `urllib` will be used by default. If you would like to use `httpx` for example, you just need to install it, and this package will automatically start using it to send API requests.

#### Automatic Configuration

By default, this package will automatically attempt to configure a http client using these libraries with the following order of preference:

For `EDClient` (sync):
1. `httpx`
2. `requests`
3. `urllib` (from the python standard library; no install required)

For `EDAsyncClient` (async):
1. `httpx`
2. `aiohttp`

#### Manual Configuration

However, you can also manually specify which of the request libraries should be used via the `http_client` parameter. 

Note: If you manually specify the `http_client` you must set `timeout` and `proxy` options on the http client rather than the EnsembleData client.

You can configure the following http clients for the `EDClient`.

```python
from ensembledata.api import EDClient, RequestsClient, HttpxClient

client = EDClient("API-TOKEN", http_client=HttpxClient())
client = EDClient("API-TOKEN", http_client=RequestsClient())
```

And you can configure the following http clients for the `EDAsyncClient`.

```python
from ensembledata.api import EDAsyncClient, AioHttpClient, HttpxAsyncClient

client = EDAsyncClient("API-TOKEN", http_client=HttpxAsyncClient())
client = EDAsyncClient("API-TOKEN", http_client=AioHttpClient())
```

<br>

### Configuring Timeout

If you would like control over the read timeout, you can configure this either for all request by setting `timeout` when creating the `EDClient`, or you can specify the `timeout` per request, on any of the individual methods as shown below.

Note: the timeout is specified in seconds and represents the total timeout for a request.

```python
from ensembledata.api import EDClient

client = EDClient("API-TOKEN", timeout=120)
result = client.tiktok.user_info_from_username(username="daviddobrik", timeout=10)
```

<br>

### Configuring Network Retries

By default the `EDClient` and `EDAsyncClient` will perform 3 retries when it encounters network issues. If you would like to customise this behaviour, you can pass in the `max_network_retries` parameter as shown below:

Note: if the request times out, it will not be retried.

```python
from ensembledata.api import EDClient

client = EDClient("API-TOKEN", max_network_retries=5)
```

<br>

### Configuring a Proxy

You can configure a proxy via the client `proxy` parameter.


Note: the timeout is specified in seconds.

```python
from ensembledata.api import EDClient

client = EDClient("API-TOKEN", proxy="http://user:pass@example.com:1234")
```

<br>

### Types

The package uses type hints, and is type checked with the latest version of `mypy`. If you experience any type checking related issues with the package, please let us know by creating an issue.
