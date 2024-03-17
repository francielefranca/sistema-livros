from django.urls import path
from . import views

app_name = 'livrosapp'

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name="register"),
    path('home/', views.home, name='home'),
]