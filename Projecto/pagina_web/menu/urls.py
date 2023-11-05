
from django.urls import path
from . import views

urlpatterns = [

    path('display/', views.display, name='display'),
    path('get_plants/', views.get_plants, name='get_plants'),
    path('get_plagas/', views.get_plagas, name='get_plagas'),
    path('', views.home, name='home'),

   

]