#!/usr/bin/bash
docker compose --env-file ./stage.env -f ./compose-stage.yml up --build -d