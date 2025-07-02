from django.urls import path
from . import views

urlpatterns = [
    path('',views.splash,name='splash'),
    path('home/', views.home_view, name='home'),
    path('stellarium/', views.stellarium, name='stellarium'),
]
