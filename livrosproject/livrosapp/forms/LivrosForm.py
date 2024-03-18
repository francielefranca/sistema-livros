from django import forms
from livrosapp.models import Livros, Genero

class LivrosForm(forms.ModelForm):

    class Meta:
        model = Livros
        fields = ['titulolivro', 'qtnpaginaslivro', 'datapublicacaolivro', 'idgenerolivro', 'idautorlivro', 'ideditoralivro']            
