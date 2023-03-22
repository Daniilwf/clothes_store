from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.upload_file, name='load_name'),

]