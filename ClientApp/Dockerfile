FROM python:3.11-slim

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x load.sh

CMD [ "./load.sh" ]