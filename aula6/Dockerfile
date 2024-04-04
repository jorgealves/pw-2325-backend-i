FROM python:3-alpine

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY . /workspace

RUN poetry install

CMD poetry run python eticbot/app.py start
