from django.urls import path
from . import views

urlpatterns = [
    path('', views.crowdfunding_view, name='crowdfunding'),
]