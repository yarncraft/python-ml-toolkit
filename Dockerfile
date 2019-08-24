FROM python:3.7.4-slim as python-base
ENV POETRY_PATH=/opt/poetry \
    VENV_PATH=/opt/venv \
    POETRY_VERSION=0.12.17
ENV PATH="$POETRY_PATH/bin:$VENV_PATH/bin:$PATH"

FROM python-base as poetry
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    \
    && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python \
    && mv /root/.poetry $POETRY_PATH \
    && poetry --version \
    \
    && python -m venv $VENV_PATH \
    && poetry config settings.virtualenvs.create false \
    \
    && rm -rf /var/lib/apt/lists/*

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi -vvv

FROM python-base as runtime
WORKDIR /app

COPY --from=poetry $VENV_PATH $VENV_PATH
COPY . ./