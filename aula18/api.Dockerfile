FROM python:3.12-slim

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /app
VOLUME [ "/app" ]
COPY . .

RUN poetry install

EXPOSE 8000 3000
