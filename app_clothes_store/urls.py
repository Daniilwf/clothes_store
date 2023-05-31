from django.urls import path
from .import views
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ex: /polls/
    path('', views.display_images, name='load_name'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:pk>', views.NewClothesStore.as_view(), name='mass-detail'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('details_views', views.details_views, name='mass-detail')


]
