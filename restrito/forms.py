from django import forms

from restrito.models import Atividade

class AtividadeForm(forms.ModelForm):

    class Meta:
        model = Atividade
        exclude = ('professor',)