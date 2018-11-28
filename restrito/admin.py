from django.contrib import admin

from restrito.models import SolicitacaoMatricula

class SolicitacaoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('disciplina_ofertada', 'aluno', 'status', 'data')
    list_filter = ('status', 'disciplina_ofertada__disciplina')
    
admin.site.register(SolicitacaoMatricula, SolicitacaoMatriculaAdmin)
