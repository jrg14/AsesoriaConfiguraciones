# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

class SignUpView(CreateView):
    form_class = SignUpForm  
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '¡Tu contraseña ha sido cambiada exitosamente!')
            return redirect('index')
        else:
            messages.error(request, 'Por favor corrige el error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})