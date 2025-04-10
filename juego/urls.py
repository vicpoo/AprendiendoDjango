from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/palabra/<str:nivel>/', views.obtener_palabra, name='obtener_palabra'),
]