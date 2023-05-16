from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.display_images, name='load_name'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:pk>', views.NewClothes_store.as_view(context_object_name= 'post'), name='post-detail')

]
