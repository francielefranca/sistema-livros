from django.shortcuts import redirect

def LoginSession(request, user):
    request.session['user_id'] = user.idusuario
    request.session['user_email'] = user.email
    print("ID USUARIO = ", user.idusuario)

    return redirect('livrosapp:home')
