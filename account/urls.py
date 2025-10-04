
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import register

urlpatterns = [


    # path('register/', views.register, name='register'),

    path('register/', register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),


]
