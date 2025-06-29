from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile_view, name='profile'),
    path('<str:username>/<int:year>/', views.profile_view, name='profile_by_year'),
]