"""Модуль для работы с очередями.

create_exchange: создание обменника.
create_queue: создание очереди.
"""

from kombu import Queue, Exchange


def create_exchange(exchange: str, exchange_type: str = 'direct') -> Exchange:
    """Создание обменника.

    Args:
        exchange (str): название обменника.
        exchange_type (str): тип обменника. По-умолчанию 'direct'

    Returns:
        Exchange: созданный обменник.
    """
    return Exchange(exchange, exchange_type)


def create_queue(_queue: str, _exchange: str | Exchange, _routing_key: str) -> Queue:
    """Создание очереди.
    Args:
        _queue (str): путь очереди.
        _exchange (str | Exchange): обменник. Если передана строка - создаст новый обменник.
        _routing_key (str): ключ.

    Returns:
        Queue: созданная очередь.
    """
    if not isinstance(_exchange, Exchange):
        _exchange = create_exchange(_exchange)
    return Queue(_queue, _exchange, _routing_key)


def create_queue_with_template(
    app_name: str,
    exchange_name: str | Exchange | None = None,
    prefix: str | None = None,
) -> Queue:
    """Создание очереди.
    Args:
        _queue (str): путь очереди.
        _exchange (str | Exchange): обменник. Если передана строка - создаст новый обменник.
        _routing_key (str): ключ.

    Returns:
        Queue: созданная очередь.
    """
    if not exchange_name:
        exchange_name = f'{prefix + "." if prefix else ""}worker.{app_name}'
    queue_name = f'{prefix + "." if prefix else ""}{app_name}.q'
    routing_key = f'{prefix + "." if prefix else ""}{app_name}'
    return create_queue(queue_name, exchange_name, routing_key)
