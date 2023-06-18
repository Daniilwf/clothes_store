from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Cloth(models.Model):
    name_of_cloth = models.TextField(max_length=50)
    path_to_image = ArrayField(models.TextField(max_length=200))
    description = models.TextField(max_length=300, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Size(models.TextChoices):
        LARGE = 'L', _('Large')
        MEDIUM = 'M', _('Medium')
        SMALL = 'S', _('Small')

    size = models.TextField(max_length=6, choices=Size.choices)
    in_stock = models.IntegerField(blank=True, null=True)
    price_with_discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_of_cloth


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE, null=True)
