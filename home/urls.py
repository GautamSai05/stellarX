from django.urls import path
from . import views

urlpatterns = [
    path('',views.splash,name='splash'),
    path('home/', views.home_view, name='home'),
    path('timeline/', views.timeline, name='timeline'),
    path('calculator/', views.calculator, name='calculator'),
    path('videos/', views.videogallery, name='videogallery'),
    path('photos/', views.photogallery, name='photogallery'),
    path('museum/', views.museum, name='museum'),
    path('starmap/', views.starmap, name='starmap'),
    path('whatif/', views.whatif, name='whatif'),
    path('women-in-space/', views.women_in_space, name='women_in_space'),
    path('feeds/', views.feeds, name='feeds'),
    path('stellarium/', views.stellarium, name='stellarium'),
]
