from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.display_images, name='load_name'),

]
