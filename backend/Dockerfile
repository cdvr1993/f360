FROM python:3.6-alpine

LABEL maintainer="cdvr1993@gmail.com"

COPY requirements.txt requirements.txt

RUN apk add --no-cache postgresql-dev gcc musl-dev && \
    pip install -r requirements.txt