from django.contrib.auth import get_user_model
from livrosapp.models import Usuario

def Authenticate(request, email, password):
    try:
        user = Usuario.objects.get(email=email)
        if user.password == password:
            return user
        else:
            return None
    except Usuario.DoesNotExist:
        return None

