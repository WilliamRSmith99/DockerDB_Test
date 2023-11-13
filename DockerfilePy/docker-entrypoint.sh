#!/bin/bash
set -e

## Call py script to validate addresses against the Smarty API
python3 /app/scripts/addressValidation.py

## Call py script to take updated db info and serve html with its contents
python3 /app/scripts/webUi.py

## Start the nginx server
nginx -g 'daemon off;'

