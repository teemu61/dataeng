FROM python:3.13 as builder
RUN apt-get -y update && apt-get -y install gcc && rm -rf /var/lib/apt/lists/*
RUN pip install poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
WORKDIR /venv
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-interaction

FROM python:3.13-slim
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*
ENV VIRTUAL_ENV=/venv/.venv
ENV PATH="/venv/.venv/bin:$PATH"
COPY --from=builder /venv/.venv /venv/.venv
COPY ./dataeng/ /dataeng/
COPY ./scripts/ /scripts/
EXPOSE 8000
ENTRYPOINT ["python3", "-m", "dataeng"]