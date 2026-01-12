from django.shortcuts import render, get_object_or_404

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
