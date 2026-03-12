import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def log_new_product_added(product_name: str, product_id: int):
    """
    Фоновая задача для логирования информации о добавлении нового товара.
    """
    message = f"Новый товар добавлен в базу данных: '{product_name}' (ID: {product_id})"
    logger.info(message)
    return message
