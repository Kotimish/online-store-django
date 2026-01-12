from django.shortcuts import render, get_object_or_404, redirect

from online_store.forms import product as product_forms
from online_store.models import Category, Product


def index(request):
    """Главная страница."""
    return render(request, 'online_store/index.html')


def about(request):
    """Страница о нас."""
    return render(request, 'online_store/about.html')


def categories_page(request):
    """Возвращает страницу со всеми категориями."""
    categories = Category.objects.all()
    context = {
        'title': 'Список категорий',
        'categories': categories,
    }
    return render(request, 'online_store/categories_list.html', context=context)


def products_page(request):
    """Возвращает страницу со всеми товарами."""
    products = Product.objects.all()
    context = {
        'title': 'Список товаров',
        'products': products,
    }
    return render(request, 'online_store/products_list.html', context=context)


def products_in_category_page(request, category_id: int):
    """Возвращает страницу со всеми товарами одной категории."""
    products = Product.objects.filter(category_id=category_id)
    context = {
        'title': 'Список товаров',
        'products': products,
    }
    return render(request, 'online_store/products_list.html', context=context)


def product_detail(request, product_id: int):
    """Возвращает страницу с подробным описанием товара."""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'title': 'Список товаров',
        'product': product,
    }
    return render(request, 'online_store/products_detail.html', context=context)


def product_add_page(request):
    """Представление для добавления нового товара"""
    if request.method == 'POST':
        form = product_forms.ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_page')
    else:
        form = product_forms.ProductModelForm()

    context = {
        'form': form,
        'title': 'Добавить товар'
    }
    return render(request, 'online_store/product_add.html', context=context)


def product_edit_page(request, product_id):
    """Представление для редактирования товара."""

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = product_forms.ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_page')
    else:
        form = product_forms.ProductModelForm(instance=product)

    context = {
        'form': form,
        'title': 'Обновить товар'
    }
    return render(request, 'online_store/product_edit.html', context=context)


def product_delete_page(request, product_id):
    """Представление для удаления Товара."""

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = product_forms.ProductDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            product.delete()
            # messages.success()
            return redirect('products_page')
    else:
        form = product_forms.ProductDeleteForm()

    context = {
        'form': form,
        'product': product,
        'title': 'Удалить товар'
    }
    return render(request, 'online_store/product_delete.html', context=context)
