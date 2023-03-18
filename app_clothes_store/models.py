import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class Cloth(models.Model):
    name_of_cloth = models.CharField(max_length=200)
    path_to_image = models.CharField(max_length=200)
    price = models.FloatField

    class Size(models.TextChoices):
        LARGE = 'LARGE', _('Large')
        MEDIUM = 'MEDIUM', _('Medium')
        SMALL = 'SMALL', _('Small')

    size = models.CharField(max_length=6, choices=Size.choices)
    in_stock = models.IntegerField

    def __str__(self):
        return self.name_of_cloth


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     @admin.display(
#         boolean=True,
#         ordering='pub_date',
#         description='Published recently?',
#     )
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
