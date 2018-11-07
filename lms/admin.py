from django.contrib import admin
from lms.models.usuarios import Aluno, Coordenador, Professor

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coordenador)