from django.db import models

from online_store.models.mixins import TimestampMixin


class Category(TimestampMixin):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()
