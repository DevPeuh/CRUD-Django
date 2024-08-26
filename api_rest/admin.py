from django.contrib import admin

# Importar os modelos para registrar no admin
from .models import Usuario

admin.site.register(Usuario)