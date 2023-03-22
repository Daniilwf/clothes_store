from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.load_name, name='index'),
]