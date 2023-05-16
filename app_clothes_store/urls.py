from django.conf.urls import include
from django.urls import path


from . import views

urlpatterns = [
    # ex: /polls/
    path('image/', views.display_clothes, name='load_name'),
    #path('user/', include('django.contrib.auth.urls'), name='update_profile')
    path('user/', views.display_user, name='update_profile'),
    path('register/', views.register, name='register'),
    path('login/', views.my_view, name='login')
]
