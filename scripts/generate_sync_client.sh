#!/bin/sh
pushd ensembledata/api
sed -e "s/Async//g" -e "s/async //g" -e "s/await //g" _async_client.py > _client.py
popd
ruff format

