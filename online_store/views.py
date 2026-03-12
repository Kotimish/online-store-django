from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from online_store.forms import product as product_forms
from online_store.models import Category, Product


from online_store.tasks import log_new_product_added


class ProductBase:
    model = Product


class CategoryBase:
    model = Category


class IndexTemplateView(TemplateView):
    template_name = 'online_store/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class AboutTemplateView(TemplateView):
    template_name = 'online_store/about.html'


class CategoriesListView(CategoryBase, ListView):
    """CBV всех категорий."""
    template_name = 'online_store/categories_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


class ProductsListView(ProductBase, ListView):
    """Страница всех товаров."""
    template_name = 'online_store/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список товаров'
        return context


class ProductsListByCategoryView(ProductBase, ListView):
    """Страница всех товаров в категории."""
    template_name = 'online_store/products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs['category_id']
        return queryset.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список товаров'
        return context


class ProductDetailView(ProductBase, DetailView):
    """Страница с подробным описанием товара."""
    template_name = 'online_store/products_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подробности товара'
        return context


class ProductCreateView(ProductBase, CreateView):
    """Страница создания товара."""
    template_name = 'online_store/product_add.html'
    form_class = product_forms.ProductModelForm
    success_url = reverse_lazy('products_page')

    def form_valid(self, form):
        """Добавляем сообщение об успешном создании товара."""
        response = super().form_valid(form)
        log_new_product_added.delay(self.object.name, self.object.id)
        messages.success(self.request, 'Новый товар успешно добавлен')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить товар'
        return context


class ProductUpdateView(ProductBase, UpdateView):
    """Представление для редактирования товара."""
    template_name = 'online_store/product_edit.html'
    form_class = product_forms.ProductModelForm
    success_url = reverse_lazy('products_page')

    def form_valid(self, form):
        """Добавляем сообщение об успешном обновлении товара."""
        messages.success(self.request, 'Товар успешно обновлен')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить товар'
        return context


class ProductDeleteView(ProductBase, DeleteView):
    """Представление для удаления Товара."""
    template_name = 'online_store/product_delete.html'
    success_url = reverse_lazy('products_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить товар'
        return context
