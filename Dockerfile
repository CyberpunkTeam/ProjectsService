FROM python:3.9-buster

RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install poetry
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install --without dev --no-interaction --no-ansi

WORKDIR /users
COPY ./ ./

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT_APP
