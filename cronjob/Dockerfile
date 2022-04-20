FROM amd64/python:3.9.7-slim

WORKDIR /app

COPY requirements.txt *.whl /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
