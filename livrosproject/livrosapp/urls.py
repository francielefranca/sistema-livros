from django.urls import path
from . import views

app_name = 'livrosapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('cadastrargenero/', views.cadastrar_genero, name='cadastrar_genero'),
    path('livros/', views.cadastrar_livro, name='livros'),
    path('livroscadastrados/', views.cadastrar_livro, name='livroscadastrados'),
    path('grupos/', views.grupos, name='grupos'),
    path('grupo/<int:grupo_id>/', views.detalhes_grupo, name='detalhes_grupo'),
    path('avaliacao/', views.avaliacao, name='avaliacao'),
    #path('detalhes_grupo/', views.grupos, name='detalhes_grupo'),
    path('recomendacao/', views.recomendacao, name='recomendacao'),
]