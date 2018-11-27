from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        abstract = True