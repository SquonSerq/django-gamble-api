#!/bin/bash
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
docker compose down