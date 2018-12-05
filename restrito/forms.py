from django import forms

from restrito.models import Atividade, AtividadeVinculada

class AtividadeForm(forms.ModelForm):

    class Meta:
        model = Atividade
        exclude = ('professor',)

class AtividadeVinculadaForm(forms.ModelForm):

    class Meta:
        model = AtividadeVinculada
        exclude = ('professor',)