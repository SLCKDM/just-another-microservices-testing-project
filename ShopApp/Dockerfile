FROM python:3.11-slim

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt requirements.txt
COPY ./local_requirements.txt local_requirements.txt

RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r local_requirements.txt --index-url http://127.0.0.1:8080/ --trusted-host 127.0.0.1

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000