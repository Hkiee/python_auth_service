FROM python:3.12-slim

ENV TZ=Europe/Moscow
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV PATH="/code/.venv/bin:$PATH"

WORKDIR /code

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --sync

COPY . /code
