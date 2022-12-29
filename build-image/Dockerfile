ARG PYTHON_VERSION=3.9.7-bullseye

FROM python:${PYTHON_VERSION}

RUN useradd -ms /bin/bash companionlabs

USER companionlabs
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

ENV PATH="/home/companionlabs/.local/bin:${PATH}"

ENTRYPOINT []
