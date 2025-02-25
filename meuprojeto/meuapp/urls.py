from django.urls import path, include
from . import views

urlpatterns = [
    path('morra/', views.morra, name='morra'),
    path('busque/', views.busque, name='busque')
]