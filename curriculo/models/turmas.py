from django.db import models

class Turma(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    nome = models.CharField(max_length=1)

    def __str__(self):
        return "{}-{}-{}".format(self.ano, self.semestre, self.nome)

    class Meta:
        unique_together = ("ano", "semestre", "nome")