from decimal import Decimal

import pytest

from online_store.models import Product


@pytest.mark.django_db
def test_product_creation(category):
    """Тест создания продукта."""
    product_name = "Новый тестовый товар"
    product_description = "Описание нового товара для теста"
    product = Product.objects.create(
        name=product_name,
        description=product_description,
        price=149.99,
        category=category
    )
    assert product.pk
    assert product.name == product_name
    assert product.description == product_description
    assert product.category == category


@pytest.mark.django_db
def test_product_read(product):
    """Тест получения существующего продукта."""
    saved_product = Product.objects.get(pk=product.pk)
    assert saved_product.name == product.name
    assert saved_product.description == product.description
    assert saved_product.price == product.price


@pytest.mark.django_db
def test_product_update(product):
    """Тест редактирования продукта."""
    update_name = "Обновленный товар"
    update_price = Decimal('199.99')
    product.name = update_name
    product.price = update_price
    product.save()

    updated_product = Product.objects.get(pk=product.pk)
    assert updated_product.name == update_name
    assert updated_product.price == update_price


@pytest.mark.django_db
def test_product_delete(product):
    """Тест удаления продукта."""
    pk = product.pk
    product.delete()

    assert not Product.objects.filter(pk=pk).exists()
