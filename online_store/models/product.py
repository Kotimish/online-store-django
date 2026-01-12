from django.db import models

from online_store.models.mixins import TimestampMixin


class Product(TimestampMixin):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    category = models.ForeignKey('online_store.Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
