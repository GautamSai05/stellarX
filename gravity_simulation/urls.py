from django.urls import path
from . import views

urlpatterns = [
    path('gravity_simulation/', views.gravity_simulation_view, name='gravity_simulation'),
]