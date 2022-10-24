# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster as dev
WORKDIR /app
COPY . .
RUN pip3 install  --no-cache-dir --upgrade -r requirements.txt
CMD ["python3", "app/blackjack.py"]

FROM python:3.8-slim-buster as testing
WORKDIR /app
COPY . .
RUN pip3 install  --no-cache-dir --upgrade -r requirements.txt
CMD ["pytest"]

# no build step required as Python isn't compiled

FROM --platform=$BUILDPLATFORM python:3.8-slim-buster
LABEL maintainer="Ade Goodyer <adriangoodyer@gmail.com>"
WORKDIR /app
COPY app/ .
COPY requirements.txt requirements.txt
RUN pip3 install  --no-cache-dir --upgrade -r requirements.txt
CMD ["python3", "blackjack.py"]
