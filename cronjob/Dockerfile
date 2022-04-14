# syntax=docker/dockerfile:1

FROM amd64/python:3.9.7-slim

WORKDIR /app

RUN apt-get update && apt-get install -y openssh-client git
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts

COPY requirements.txt *.whl /app/

RUN --mount=type=ssh pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app
