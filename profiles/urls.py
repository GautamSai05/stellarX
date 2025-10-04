from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile_view, name='profile'),
    path('search/', views.user_search, name='profile_user_search'),
    
]