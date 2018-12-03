from django.contrib import admin

from restrito.models import SolicitacaoMatricula

class SolicitacaoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('disciplina_ofertada', 'aluno', 'status', 'data')
    list_filter = ('status', 'disciplina_ofertada__disciplina')
    fields = ('aluno', 'disciplina_ofertada', 'coordenador', 'status')
    readonly_fields = ('aluno', 'disciplina_ofertada', 'coordenador')

    def save_model(self, request, obj, form, change):
        obj.coordenador = request.user.coordenador
        super(SolicitacaoMatriculaAdmin, self).save_model(request, obj, form, change)
    
admin.site.register(SolicitacaoMatricula, SolicitacaoMatriculaAdmin)
