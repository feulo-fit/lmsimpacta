from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    sigla = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.nome