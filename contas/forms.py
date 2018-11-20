from django import forms

from contas.models import Aluno, Professor

class LoginForm(forms.Form):

    login = forms.CharField(
        max_length=100,
        label="Usuário"
    )

    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput
    )

class AlunoCriacaoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('login', 'nome', 'email', 'celular')

class UsuarioAlteracaoForm(forms.ModelForm):
    senha1 = forms.CharField(
        label = "Senha",
        widget=forms.PasswordInput,
        required=False,
        help_text='Informe apenas se quiser alterar'
    )
    senha2 = forms.CharField(
        label="Confirme sua senha",
        widget=forms.PasswordInput,
        required=False,
        help_text='As senhas devem ser iguais'
    )

    def clean_senha2(self):
        senha1 = self.cleaned_data['senha1']
        senha2 = self.cleaned_data['senha2']
        if senha1 and senha1 != senha2:
            raise forms.ValidationError('As senhas devem ser iguais.')

        return senha2

    def save(self, commit=True):
        usu = super(UsuarioAlteracaoForm, self).save(False)
        senha1 = self.cleaned_data['senha1']
        if senha1:
            usu.set_password(senha1)
        usu.save()
        return usu

class AlunoAlteracaoForm(UsuarioAlteracaoForm):
    class Meta:
        model = Aluno
        fields = ('login', 'nome', 'email', 'celular', 'foto')

class ProfessorAlteracaoForm(UsuarioAlteracaoForm):
    class Meta:
        model = Professor
        fields = ('login', 'nome', 'email', 'celular', 'apelido')