from django.urls import path, re_path, include
from . import views
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ex: /polls/
    path('', views.main, name='main'),
    # path('accounts', include('django.contrib.auth.urls')),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:pk>', views.NewClothesStore.as_view(), name='mass-detail'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('discounts', views.discounts, name='discounts'),
    path('assortment', views.assortment, name='assortment'),
    re_path(r'^cart/', views.cart_detail, name='CartDetail'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='CartAdd'),
    path('favorites', views.output_favorites, name='favorites'),
    re_path(r'^add-to-favorite/(?P<cloth_id>\d+)/$', views.add_to_favorite, name='add_to_favorite'),
    re_path(r'^delete-from-favorite/(?P<cloth_id>\d+)/$', views.delete_from_favorite, name='delete_from_favorite'),
    # path('details_views', views.details_views, name='mass-detail')

]
