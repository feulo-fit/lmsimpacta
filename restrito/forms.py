from django import forms
from django.contrib.admin import widgets

from bootstrap_datepicker_plus import DateTimePickerInput

from restrito.models import Atividade, AtividadeVinculada, Entrega, SolicitacaoMatricula

class AtividadeForm(forms.ModelForm):

    class Meta:
        model = Atividade
        exclude = ('professor',)

class AtividadeVinculadaForm(forms.ModelForm):

    def __init__(self, professor, *args, **kwargs):
        super(AtividadeVinculadaForm, self).__init__(*args, **kwargs)
        self.fields['atividade'].queryset = Atividade.objects.filter(professor=professor)
        
    class Meta:
        model = AtividadeVinculada
        exclude = ('professor', 'disciplina_ofertada', 'status')
        widgets = {
            'data_inicio': DateTimePickerInput(
                options={
                    "format":"DD/MM/YYYY HH:mm"
                }
            ),
            'data_fim': DateTimePickerInput(
                options={
                    "format":"DD/MM/YYYY HH:mm"
                }
            ),
        }

class EntregaAlunoForm(forms.ModelForm):

    class Meta:
        model = Entrega
        fields = ('titulo', 'resposta')

class SolicitacaoMatriculaForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoMatricula
        fields = ('disciplina_ofertada',)