# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app/api

COPY ../requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# ENV FLASK_DEBUG 1

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# COPY ./api /app/api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]