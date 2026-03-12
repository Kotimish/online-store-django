from unittest.mock import patch

import pytest
from django.test import Client
from django.urls import reverse

from online_store.models import Product, Category
from online_store.tasks import log_new_product_added


@pytest.mark.django_db
def test_log_new_product_added():
    """
    Проверка логики внутри задачи Celery (логирование сообщения).
    """

    product_name = "Тестовый товар"
    product_id = 999
    expected_message = f"New product added to the database: '{product_name}' (ID: {product_id})"

    # Вызов задачи напрямую, как обычную функцию
    result = log_new_product_added(product_name, product_id)
    # Сверка сообщений
    assert result == expected_message


@pytest.mark.django_db
@patch("online_store.views.log_new_product_added.delay")
def test_product_create_calls_celery_task(mock_task_delay):
    """
    Тест вызова задачи Celery при создании продукта
    """
    client = Client()

    # Создание тестовых данных
    category = Category.objects.create(
        name="Тестовая категория",
        description="Описание тестовой категории"
    )
    product_data = {
        "name": "Тестовый товар",
        "description": "Описание тестового товара",
        "price": 149.99,
        "category": category.id,
    }

    # Отправляем POST-запрос на создание
    url = reverse('post_add')
    response = client.post(url, data=product_data)

    # Проверка статуса запроса
    assert response.status_code in [200, 302]

    # Проверка, что вызов был только один
    mock_task_delay.assert_called_once()

    # Проверка аргументов
    created_product = Product.objects.get(name=product_data['name'])
    mock_task_delay.assert_called_with(created_product.name, created_product.id)
