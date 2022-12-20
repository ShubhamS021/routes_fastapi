ARG PYTHON_VERSION=3.9.7-bullseye

FROM python:${PYTHON_VERSION}

RUN useradd -ms /bin/bash companionlabs

USER companionlabs
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

ENV PATH="/home/companionlabs/.local/bin:${PATH}"

WORKDIR /class-fastapi

ADD check.sh /class-fastapi/
ADD .flake8 /class-fastapi/
ADD pytest.ini /class-fastapi/
ADD README.md /class-fastapi/
ADD pyproject.toml /class-fastapi/
ADD poetry.lock /class-fastapi/

RUN poetry install

ADD classy_fastapi/ /class-fastapi/classy_fastapi/

CMD ["./check.sh"]
