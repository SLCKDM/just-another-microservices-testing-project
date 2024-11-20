FROM python:3.11

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y libpq-dev gcc curl \
    && rm -rf /var/lib/apt/lists/*

COPY .pypirc /root/.pypirc

COPY . .

RUN pip install --upgrade build
RUN pip install . -U
# RUN python3 -m build
RUN chmod +x upload.sh
CMD ["./upload.sh"]
