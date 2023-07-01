from django.urls import path
from .views import logIn, registro, dashboard, perfil, perfilt, like_user, dislike_user, chat

urlpatterns = [
    path('', logIn, name='logIn'),
    path('registro', registro, name='registro'),
    path('dashboard', dashboard, name='dashboard'),
    path('perfil', perfil, name='perfil'),
    path('perfilt', perfilt, name='perfilt'),
    path('like/<int:matched_user_id>/', like_user, name='like_user'),
    path('dislike/<int:matched_user_id>/', dislike_user, name='dislike_user'),
    path('chat/<int:chat_id>/', chat, name='chat'),
]
