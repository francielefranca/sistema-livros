# No seu arquivo forms.py
from django import forms
from livrosapp.models import Genero

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['idgenero', 'nome']
