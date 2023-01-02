#!/bin/bash

# Simple script to build our various container versions and push them. It takes one argument: the first part of the tag.
# If the argument is v004 for example this will be v004-py3.11 and v004-py3.9 for our two different python versions.

CONTAINER_BASE=registry.gitlab.com/companionlabs-opensource/classy-fastapi

docker build -t $CONTAINER_BASE:$1-py3.11 --build-arg PYTHON_VERSION=3.11.1-bullseye .
docker build -t $CONTAINER_BASE:$1-py3.9 --build-arg PYTHON_VERSION=3.9.7-bullseye .

docker push $CONTAINER_BASE:$1-py3.11
docker push $CONTAINER_BASE:$1-py3.9 
