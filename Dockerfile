FROM python:3.8.5

WORKDIR /code

COPY requirements.txt /code

RUN pip3 install -r /code/requirements.txt

COPY . /code

ENV DB_ENGINE django.db.backends.postgresql
ENV DB_NAME postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD notpostgrespass
ENV DB_HOST db
ENV DB_PORT 5432

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000 
