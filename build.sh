#!/bin/bash

APP_NAME="EVENT API"

case $1 in
	prod)	ENV=prod;;
	dev)	ENV=dev;;
	*)		echo "Invalid environment"
			echo "bash build.sh <env>"
			echo "env: dev | prod"
			exit;;
esac

echo "------------------------------------------------"
echo "Running ${APP_NAME} | Environment: $ENV "
echo "------------------------------------------------"
echo ""

export EVENT_API_ENV=$ENV

python event_api.py