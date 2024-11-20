from shop_core_utils.queues import create_queue_with_template

from settings import APP_NAME

queue = create_queue_with_template(APP_NAME, exchange_name="worker.notifier", prefix="notifier")
