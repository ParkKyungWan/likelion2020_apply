from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from .views import IndexView, profile, add, remove



# from . import views 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('cart/add/<int:id>', add, name='add'),
    path('cart/remove/<int:id>', add, name='remove')
]