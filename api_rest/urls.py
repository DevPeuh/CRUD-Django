from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_usuarios, name='get_todos_usuarios'),  # Quando o usuário acessar /api, vai devolver todos os usuários
    path('usuario/<int:id>/', views.get_por_id, name='get_usuario_por_id'),  # Acessa um usuário específico pelo ID
    path('data/', views.gerenciador_usuario, name='gerenciar_usuario')  # Endpoint para gerenciar usuários (GET, POST, PUT, DELETE)
]
