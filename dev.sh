#!/usr/bin/bash
docker compose --env-file ./local.env -f ./compose-dev.yml up --build