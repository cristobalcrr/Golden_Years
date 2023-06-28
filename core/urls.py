from django.urls import path
from core import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('chat/', views.chat, name='chat'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
]
