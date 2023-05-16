from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Cloth(models.Model):
    name_of_cloth = models.TextField(max_length=200)
    path_to_image = ArrayField(models.TextField(max_length=300))
    price = models.FloatField(blank=True)

    class Size(models.TextChoices):
        LARGE = 'Large', _('Large')
        MEDIUM = 'Medium', _('Medium')
        SMALL = 'Small', _('Small')

    size = models.TextField(max_length=6, choices=Size.choices)
    in_stock = models.IntegerField(blank=True)

    def __str__(self):
        return self.name_of_cloth


class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='client')
    country = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    address = models.TextField(max_length=200)

    def __str__(self):
        if self.user is not None:
            return self.user.get_username()
        else:
            return "Empty username"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)
    instance.client.save()

#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         client = Client(user=user)
#         client.save()
