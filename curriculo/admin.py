from django.contrib import admin

from curriculo.models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome', 'sigla')

admin.site.register(Curso, CursoAdmin)
