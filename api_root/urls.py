from django.contrib import admin
from django.urls import path, include # include para incluir no navegador

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls'), name='api_rest_urls') # para buscar as funções do app
]
