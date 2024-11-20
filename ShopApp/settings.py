import os
from shop_core_utils.queues import create_queue_with_template


RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PORT = os.getenv("RMQ_PORT")
RMQ_USER = os.getenv("RMQ_USER")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD")
RMQ_VHOST = os.getenv("RMQ_VHOST")
RMQ_LOG = os.getenv("RMQ_LOG")
RMQ_URL = f"pyamqp://{RMQ_USER}:{RMQ_PASSWORD}@{RMQ_HOST}:{RMQ_PORT}/{RMQ_VHOST}"


email_queue = create_queue_with_template("email_notifications", "notifier")
