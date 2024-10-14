from django.urls import path
from. import views

urlpatterns = [
    
    path('ver_usuarios/', views.ver_usuarios, name='ver_usuarios'),
]
