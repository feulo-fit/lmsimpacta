from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1), blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, default=None)

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)

    class Meta:
        abstract = True

class Coordenador(Usuario, Pessoa):
    pass

class Aluno(Usuario, Pessoa):
    ra = models.CharField(max_length=20, unique=True)
    foto = models.CharField(max_length=255, default=None, blank=True, null=True)

class Professor(Usuario, Pessoa):
    apelido = models.CharField(max_length=255)

