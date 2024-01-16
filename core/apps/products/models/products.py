from django.db import models

from core.apps.common.models import TimedBasedModel


class Product(TimedBasedModel):
    title = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара", blank=True)
    is_visible = models.BooleanField(default=True, verbose_name="Показывать товар")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title
