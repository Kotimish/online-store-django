from decimal import Decimal

from django.contrib import admin
from django.contrib import messages
from django.db import models

from online_store.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at', 'updated_at']
    ordering = ['-created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    search_help_text = 'Введите часть названия или описания'
    list_per_page = 20

    fields = ('name', 'price', 'category', 'tags', 'created_at', 'updated_at')

    @admin.action(description='Увеличить цену на 10 процентов')
    def increase_price_by_ten_percent(self, request, queryset):
        updated_count = queryset.update(price=models.F('price') * Decimal('1.1'))
        self.message_user(
            request,
            f'Обновлено товаров: {updated_count}',
            messages.SUCCESS
        )

    @admin.action(description='Уменьшить цену на 10 процентов')
    def reduce_price_by_ten_percent(self, request, queryset):
        updated_count = queryset.update(price=models.F('price') * Decimal('0.9'))
        self.message_user(
            request,
            f'Обновлено товаров: {updated_count}',
            messages.SUCCESS
        )

    actions = (
        increase_price_by_ten_percent,
        reduce_price_by_ten_percent,
    )
