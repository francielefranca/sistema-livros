from django.shortcuts import redirect, render

from .forms.UserCreationForm import UserCreationForm
#from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home.html')
        
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'livrosapp/home.html')