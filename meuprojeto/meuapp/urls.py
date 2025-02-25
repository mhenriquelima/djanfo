from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('cars/', views.ListarMarcas, name='carros')
]