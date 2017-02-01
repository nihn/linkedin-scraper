#!/bin/sh

exec docker-compose run --entrypoint pytest crawler "$@"
