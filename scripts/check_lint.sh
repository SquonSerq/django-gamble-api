#!/bin/bash
flake8 --exclude ./gamble_api/gamble_api,migrations ./gamble_api/
echo Lint checked.