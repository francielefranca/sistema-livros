from django import forms
from livrosapp.models import Usuario

class UserCreationForm(forms.Form):
    #idusuario = forms.IntegerField()
    nome = forms.CharField(label="Nome", max_length=150)
    apelido = forms.CharField(label="Apelido", max_length=150)
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    leituras = forms.CharField(label="Leituras", max_length=500)
    #lider = forms.BooleanField(label="Lider de Grupo", required=False)
    idgenero = forms.CheckboxSelectMultiple()

    class Meta:
        model = Usuario
        fields = ['idusuario', 'nome', 'email', 'password', 'apelido', 'leituras', 'idgenero']
        exclude = ['lider']
