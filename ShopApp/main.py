from celery import Celery
from fastapi import FastAPI

from shop_core_utils.tasks import call_task

from settings import RMQ_URL

celery = Celery(broker=RMQ_URL)
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/ping')
async def call_ping():
    msg = {}
    try:
        call_task(
            '*_notifications.tasks.ping',
            exchange='worker.notifier'
        )
        msg = {'ping': 'sent'}
    except Exception as exc:
        msg = {'ping': str(exc)}

    return msg

