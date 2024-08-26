from django.db import models

class Usuario(models.Model):
    # Definir quais serão os campos que estarão dentro do banco de dados
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=150, default='')
    email_usuario = models.EmailField(default='')
    idade_usuario = models.IntegerField(default=0)

    def __str__(self):
        return f'ID usuário: {self.id_usuario} | Nome usuário: {self.nome_usuario} | E-mail: {self.email_usuario}'