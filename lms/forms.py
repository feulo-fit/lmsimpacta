from django import forms
from django.conf import settings
from django.core.mail import send_mail

ASSUNTOS = (
    ('', ' - Selecione um - '),
    ('B', 'Bug'),
    ('R', 'Reclamação'),
    ('S', 'Sugestão')
)

class ContatoForm(forms.Form):

    nome = forms.CharField(
        label="Nome Completo"
    )

    email = forms.EmailField(
        label="E-Mail"
    )

    assunto = forms.ChoiceField(
        label="Assunto",
        choices=ASSUNTOS
    )

    mensagem = forms.CharField(
        label="Mensagem",
        max_length=255,
        widget=forms.Textarea
    )

    def enviar_email(self):
        assunto = self.cleaned_data['assunto']
        send_mail(
            'Mensagem Assunto '+dict(ASSUNTOS)[assunto],
            self.cleaned_data['mensagem'],
            self.cleaned_data['email'],
            [settings.EMAIL_CONTATO]
        )