import pytest

from online_store.models import Category, Product


@pytest.fixture
def category():
    """Фикстура для создания тестовой категории."""
    return Category.objects.create(
        name="Тестовая категория",
        description="Описание тестовой категории"
    )


@pytest.fixture
def product(category):
    """Фикстура для создания тестового продукта, связанного с категорией."""
    return Product.objects.create(
        name="Тестовый товар",
        description="Описание тестового товара",
        price=100.00,
        category=category
    )
