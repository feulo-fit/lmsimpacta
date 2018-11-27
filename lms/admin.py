from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#from lms.models.usuarios import Usuario, Aluno, Coordenador, Professor
#from lms.models.disciplinas import Curso, Disciplina, DisciplinaOfertada, SolicitacaoMatricula, Turma
from lms.models.atividades import Atividade, AtividadeVinculada, Entrega

# Register admin behavior
#class UsuarioInline(admin.StackedInline):
#    model = Usuario
#    can_delete = False
#    verbose_name_plural = 'usuários'

# Re-register UserAdmin
#class UserAdmin(BaseUserAdmin):
#    inlines = (UsuarioInline,)

# Register your models here.
#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

#admin.site.register(Aluno)
#admin.site.register(Professor)
#admin.site.register(Coordenador)

#admin.site.register(Curso)
#admin.site.register(Disciplina)
#admin.site.register(DisciplinaOfertada)
#admin.site.register(SolicitacaoMatricula)
#admin.site.register(Turma)

admin.site.register(Atividade)
admin.site.register(AtividadeVinculada)
admin.site.register(Entrega)
