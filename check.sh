#!/bin/bash

# Simple shell script to run unit tests, MyPy and flake8

poetry install
poetry run pytest -s
poetry run mypy -p routes_fastapi
poetry run flake8
