import pytest

from online_store.models import Category


@pytest.mark.django_db
def test_category_create():
    """Тест создания новой категории."""
    category_name = "Новая категория для теста"
    category_description = "Описание новой категории для теста"
    category = Category.objects.create(
        name=category_name,
        description=category_description
    )
    assert category.name == category_name
    assert category.description == category_description


@pytest.mark.django_db
def test_category_read(category):
    """Тест получения существующей категории."""
    saved_category = Category.objects.get(pk=category.pk)
    assert saved_category.name == category.name
    assert saved_category.description == category.description


@pytest.mark.django_db
def test_category_update(category):
    """Тест редактирования категории."""
    update_name = "Обновленная категория"
    category.name = update_name
    category.save()

    updated_category = Category.objects.get(pk=category.pk)
    assert updated_category.name == update_name


@pytest.mark.django_db
def test_category_delete(category):
    """Тест удаления категории."""
    pk = category.pk
    category.delete()
    assert not Category.objects.filter(pk=pk).exists()
