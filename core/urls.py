from django.urls import path
from .views import login, registro, dashboard, perfil, chat, enviar_mensaje, perfilt, like_user, dislike_user, chatp

urlpatterns = [
    path('', login, name='login'),
    path('registro', registro, name='registro'),
    path('dashboard', dashboard, name='dashboard'),
    path('perfil', perfil, name='perfil'),
    path('chat', chat, name='chat'),
    path('enviar', enviar_mensaje, name='enviar_mensaje'),
    path('perfilt', perfilt, name='perfilt'),
    path('like/<int:matched_user_id>/', like_user, name='like_user'),
    path('dislike/<int:matched_user_id>/', dislike_user, name='dislike_user'),
    path('chat/<int:chat_id>/', chat, name='chat'),
]
