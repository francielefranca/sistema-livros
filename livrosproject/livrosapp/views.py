#importando funcoes django
from django.shortcuts import get_object_or_404, redirect, render

#importando forms
from .forms.UserCreationForm import UserCreationForm
from .forms.UserLoginForm import UserLoginForm
from .forms.LivrosForm import LivrosForm
from .forms.GeneroForm import GeneroForm

#importando models
from .models import Autor, Avaliacao, Editora, Genero, Grupo, Livros, Participantes, Publicacao, Usuario 

#importando funcoes uteis
from .utils.Authenticate import Authenticate
from .utils.LoginSession import LoginSession

def home(request):
    try:
        return render(request, 'livrosapp/home.html')
    
    except Usuario.DoesNotExist:
        print("Usuário não encontrado")
        return redirect('livrosapp:login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            idusuario = form.cleaned_data['idusuario']
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            apelido = form.cleaned_data['apelido']
            leituras = form.cleaned_data['leituras']
            idgenero = form.cleaned_data['idgenero']

            usuario = Usuario(idusuario=idusuario, nome=nome, email=email, password=password, apelido=apelido, leituras=leituras, idgenero=idgenero)
            usuario.save()
            print(usuario)
            return redirect('livrosapp:home') 
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():  
            email = form.cleaned_data.get('email')  
            password = form.cleaned_data.get('password')  

            user = Authenticate(request, email=email, password=password)
            if user is not None:
                print("O LOGIN FUNCIONOU")
                print(user)
                LoginSession(request, user)
                return redirect('livrosapp:home')
            else:
                print("Credenciais inválidas")
                return redirect('livrosapp:login')
        else:
            print("Formulário inválido")
            return redirect('livrosapp:login')
    else:
        form = UserLoginForm()

    return render(request, 'registration/login.html', {'form': form})

def cadastrar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()  
            #return redirect('lista_generos')  
    else:
        form = GeneroForm()

    return render(request, 'livrosapp/genero.html', {'form': form})

def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livrosapp/livroscadastrados.html')
    else:
        form = LivrosForm()
    return render(request, 'livrosapp/livros.html', {'form':form})

def livros(request):
    livros = Livros.objects.all()
    return render(request, 'livrosapp/livroscadastrados.html', {'livros': livros})

def grupos(request):
    if request.method == 'POST':
        nome_grupo = request.POST.get('nome_grupo')
        genero_id = request.POST.get('genero_id')

        novo_grupo = Grupo.objects.create(nomegrupo=nome_grupo, idgenerogrupo=genero_id)

        return redirect('livrosapp/detalhes_grupo.html', grupo_id=novo_grupo.id)
    else:
        grupos = Grupo.objects.all()
    return render(request, 'livrosapp/grupo.html', {'grupos':grupos})

def detalhes_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk=grupo_id) 

    return render(request, 'livrosapp/detalhes_grupo.html', {'grupo': grupo})

def avaliacao(request):
    a
    
def recomendacao(request):
    generos = Genero.objects.all()

    if request.method == 'POST':
        qtd_paginas = request.POST.get('qtd_paginas')
        genero_id = request.POST.get('genero_id')

        livros = Livros.objects.filter(qtnpaginaslivro__lte=qtd_paginas, idgenerolivro=genero_id)[:3]
        print(livros)
        return render(request, 'livrosapp/recomendacao.html', {'livros': livros, 'generos': generos})
    else:
        return render(request, 'livrosapp/recomendacao.html', {'generos': generos})
