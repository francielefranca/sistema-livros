from django import forms
from livrosapp.models import Usuario

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['idusuario', 'nome', 'email', 'password', 'apelido', 'leituras', 'idgenero']
        exclude = ['lider']
