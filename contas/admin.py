from django.contrib import admin
from django.contrib.auth.models import Group

from contas.models import Coordenador, Professor, Aluno

class UsuarioAdmin(admin.ModelAdmin):
    # Tipo de usuário (C, A ou P)
    _tipo = None
    extra_fields = []
    list_display = ['nome', 'email', 'celular']
    fields = ['login', 'dt_expiracao', 'nome', 'email', 'celular']
    
    def get_fields(self, request, obj=None):
        return super(UsuarioAdmin, self).get_fields(request, obj) + self.extra_fields

    def get_list_display(self, request):
        return self.list_display + self.extra_fields

    def save_model(self, request, obj, form, change):
        obj.tipo = self._tipo
        obj.set_password('123@mudar')
        super().save_model(request, obj, form, change)

class ProfessorAdmin(UsuarioAdmin):
    _tipo = 'P'
    extra_fields = ['apelido']

class AlunoAdmin(UsuarioAdmin):
    _tipo = 'A'
    extra_fields = ['ra']

class CoordenadorAdmin(UsuarioAdmin):
    _tipo = 'C'

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Coordenador, CoordenadorAdmin)
# Register your models here.
admin.site.unregister(Group)
