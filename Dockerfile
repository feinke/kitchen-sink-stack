# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements-base.txt requirements-base.txt

RUN pip3 install -r requirements-base.txt

COPY api/app.py app.py

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]