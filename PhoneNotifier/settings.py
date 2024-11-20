import os

APP_NAME = "phone_notifications"

RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PORT = os.getenv("RMQ_PORT")
RMQ_USER = os.getenv("RMQ_USER")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD")
RMQ_VHOST = os.getenv("RMQ_VHOST")
RMQ_LOG = os.getenv("RMQ_LOG")
RMQ_URL = f"pyamqp://{RMQ_USER}:{RMQ_PASSWORD}@{RMQ_HOST}:{RMQ_PORT}/{RMQ_VHOST}"
