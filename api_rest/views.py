from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer

import json

@api_view(['GET'])
def get_usuarios(request):
   
    usuarios = Usuario.objects.all()  # Vai no banco de dados e vai devolver todos os objetos (retornando um queryset)
    
    serializer = UsuarioSerializer(usuarios, many=True)  # Serializa todos os objetos puxados acima
   
    return Response(serializer.data)  # Retorna os dados serializados


@api_view(['GET', 'PUT'])
def get_por_id(request, id):
    
    try:
       
        usuario = Usuario.objects.get(pk=id)  # Tenta recuperar o usuário do banco de dados pelo ID
   
    except Usuario.DoesNotExist:
       
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)  # Caso não seja encontrado

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)  # Serializa o objeto Usuario para JSON
        return Response(serializer.data)  # Retorna os dados serializados

    if request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerenciador_usuario(request):
   
    if request.method == 'GET':
       
        id_usuario = request.GET.get('usuario')  # Obtém o valor do parâmetro 'usuario' da URL, se existir
       
        if id_usuario:
           
            try:
           
                usuario = Usuario.objects.get(pk=id_usuario)  # Tenta obter o objeto Usuario com o ID fornecido
           
                serializer = UsuarioSerializer(usuario)  # Serializa o objeto Usuario para JSON
           
                return Response(serializer.data)  # Retorna os dados serializados
          
            except Usuario.DoesNotExist:
          
                return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
       
        else:
          
            return Response({'error': 'ID do usuário não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

# CRIAR DADOS
    elif request.method == 'POST': 
        novo_usuario = request.data  # Obtém os dados do novo usuário da requisição
        
        serializer = UsuarioSerializer(data=novo_usuario)  # Serializa os dados do novo usuário
        
        if serializer.is_valid():  # Verifica se os dados são válidos
            
            serializer.save()  # Salva os dados no banco de dados
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna os dados do usuário criado
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Requisição inválida



# EDITAR DADOS
    elif request.method == 'PUT':
       
        id = request.data.get('id_usuario')  # Obtém o ID do usuário a partir dos dados da requisição
        
        try:
       
            atualizar_usuario = Usuario.objects.get(pk=id)  # Tenta recuperar o usuário do banco de dados pelo ID
      
        except Usuario.DoesNotExist:
       
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

      
        serializer = UsuarioSerializer(atualizar_usuario, data=request.data)  # Cria um serializer com os dados do usuário e os novos dados da requisição
      
        if serializer.is_valid():  # Verifica se os dados fornecidos são válidos
        
            serializer.save()  # Se forem válidos, salva as alterações no banco de dados
         
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)  # Retorna os dados atualizados
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Requisição inválida



# DELETAR DADOS 
    elif request.method == 'DELETE':
      
        id = request.data.get('id_usuario')  # Obtém o ID do usuário a partir dos dados da requisição
      
        try:
       
            usuario = Usuario.objects.get(pk=id)  # Tenta recuperar o usuário do banco de dados pelo ID
       
            usuario.delete()  # Deleta o usuário do banco de dados
       
            return Response(status=status.HTTP_204_NO_CONTENT)  # Retorna um status 204 (sem conteúdo)
      
        except Usuario.DoesNotExist:
       
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)  # Retorna um status 400 se o método não for suportado
