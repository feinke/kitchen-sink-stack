# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements-base.txt requirements-base.txt

RUN pip3 install -r requirements-base.txt

WORKDIR /api

COPY api/main.py main.py

ENV PYTHONPATH /api

CMD ["main.py"]