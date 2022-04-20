FROM amd64/python:3.9.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]