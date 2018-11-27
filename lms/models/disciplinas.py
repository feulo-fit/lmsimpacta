from django.db import models
from django.utils import timezone

from contas.models import Aluno, Coordenador, Professor
'''
class Disciplina(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    data = models.DateField(default=timezone.now, blank=True, null=True)
    status = models.CharField(max_length=50, default='Aberta', blank=True, null=True)
    plano_ensino = models.TextField(max_length=500)
    carga_horaria = models.IntegerField()
    competencias = models.TextField(max_length=500)
    habilidades = models.TextField(max_length=500)
    ementa = models.TextField(max_length=500)
    conteudo_programatico = models.TextField(max_length=500)
    bibliografia_basica = models.TextField(max_length=500)
    bibliografia_complementar = models.TextField(max_length=500)
    percentual_pratico = models.IntegerField()
    percentual_teorico = models.IntegerField()
    coordenador = models.ForeignKey(Coordenador, models.PROTECT)

class Curso(models.Model):
    nome = models.CharField(max_length=255, unique=True)

class Turma(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    nome = models.CharField(max_length=1)

    class Meta:
        unique_together = ("ano", "semestre", "nome")

class DisciplinaOfertada(models.Model):
    coordenador = models.ForeignKey(Coordenador, models.PROTECT)
    curso = models.ForeignKey(Curso, models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, models.PROTECT)
    turma = models.ForeignKey(Turma, models.PROTECT)
    dt_inicio_matricula = models.DateField()
    dt_fim_matricula = models.DateField()
    professor = models.ForeignKey(Professor, models.PROTECT, default=None, blank=True, null=True)
    metodologia = models.TextField(max_length=500, default=None, blank=True, null=True)
    recursos = models.TextField(max_length=500, default=None, blank=True, null=True)
    criterio_avaliacao = models.TextField(max_length=500, default=None, blank=True, null=True)
    plano_aulas = models.TextField(max_length=500, default=None, blank=True, null=True)

    class Meta:
        unique_together = ("disciplina", "curso", "turma")

class SolicitacaoMatricula(models.Model):
    aluno = models.ForeignKey(Aluno, models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, models.PROTECT)
    coordenador = models.ForeignKey(Coordenador, models.PROTECT, default=None, blank=True, null=True)
    data = models.DateField(default=timezone.now, blank=True, null=True, editable=False)
    status = models.CharField(max_length=50, default='Solicitada', blank=True, null=True)

'''