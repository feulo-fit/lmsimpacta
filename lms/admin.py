from django.contrib import admin
from lms.models.usuarios import Aluno, Coordenador, Professor
from lms.models.disciplinas import Curso, Disciplina, DisciplinaOfertada, SolicitacaoMatricula, Turma
from lms.models.atividades import Atividade, AtividadeVinculada, Entrega

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coordenador)

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)
admin.site.register(SolicitacaoMatricula)
admin.site.register(Turma)

admin.site.register(Atividade)
admin.site.register(AtividadeVinculada)
admin.site.register(Entrega)
