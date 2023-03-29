from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cloth(models.Model):
    name_of_cloth = models.TextField(max_length=200)
    path_to_image = ArrayField(models.TextField(max_length=300))
    price = models.FloatField

    class Size(models.TextChoices):
        LARGE = 'LARGE', _('Large')
        MEDIUM = 'MEDIUM', _('Medium')
        SMALL = 'SMALL', _('Small')

    size = models.TextField(max_length=6, choices=Size.choices)
    in_stock = models.IntegerField

    def __str__(self):
        return self.name_of_cloth
