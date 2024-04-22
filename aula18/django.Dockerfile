FROM python:3.12-slim

RUN pip install poetry


WORKDIR /app

COPY ./django/ .

RUN poetry install --no-root

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
