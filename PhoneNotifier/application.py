from celery import Celery

from queues import queue
from settings import (
    APP_NAME, RMQ_URL
)


app = Celery(
    APP_NAME,
    broker=RMQ_URL,
    include=[
        f'{APP_NAME}.tasks',
        # f'{APP_NAME}.',
    ]
)

app.conf.task_queues = (
    queue,
)


if __name__ == "__main__":
    app.start()
