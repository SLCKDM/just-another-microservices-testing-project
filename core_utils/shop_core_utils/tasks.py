from celery import current_app
from kombu import Queue, Exchange

def call_task(
    name: str,
    queue: str | Queue | None = None,
    exchange: str | Exchange | None = None,
    args: tuple | None = None,
    kwargs: dict | None = None
):
    """Вызывает задачу :name: для очереди :queue:.

    Args:
        name (str): .
        queue (str | Queue): .
        args (tuple): .
        kwargs (dict): .
    """
    current_app.send_task(
        name, queue=queue, exchange=exchange, args=args or (), kwargs=kwargs or {}
    )
