#!/bin/sh
pushd ensembledata/api
sed -e "s/Async//g" -e "s/async //g" -e "s/await //g" async_client.py > client.py
popd

