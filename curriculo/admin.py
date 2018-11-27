from django.contrib import admin

from curriculo.models import Curso, Disciplina, Turma, DisciplinaOfertada

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome', 'sigla')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'status', 'coordenador', 'percentual_pratico', 'percentual_teorico')
    search_fields = ('nome',)
    list_filter = ('coordenador', 'status', 'carga_horaria')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('ano', 'semestre', 'nome')
    list_filter = ('ano', 'semestre', 'nome')

@admin.register(DisciplinaOfertada)
class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'turma', 'curso', 'professor')
    search_fields = ('disciplina__nome', 'curso__nome')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)