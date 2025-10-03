from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.profile_settings_view, name='profile_settings'),
    path('<str:username>/', views.profile_view, name='profile'),
]