from django import forms
from livrosapp.models import Usuario

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'password']
        exclude = ['idusuario', 'nome', 'apelido', 'leituras', 'idgenero', 'lider']