from rest_framework import serializers

from .models import Usuario

# Criar a classe com o nome que quer serializar
class UsuarioSerializer(serializers.ModelSerializer):
    # Criar a classe Meta para colocar qual modelo e qual campo serão serializados
    class Meta:
        model = Usuario
        fields = '__all__' # Para a API devolver todos os campos