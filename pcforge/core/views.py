from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from core.models import bd_manager
from django.contrib.auth.decorators import login_required
from core.forms import ContactForm

bd = bd_manager()

def index(request):
        bd.actualizar_visitas()
        return render(request, "content/initialBody.html",{})

def about(request):
        return render(request, "content/about.html",{})

def ensamblador(request):
    context = {
        'is_authenticated': request.user.is_authenticated,
    }
    return render(request, "content/ensamblador.html", context)


@login_required
def configuraciones(request):
        return render(request, "content/configuraciones.html", {})

@login_required
def DatosUsuario(request):
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        
        return render(request, "content/DatosUsuario.html",{'username':username, 'first_name':first_name, 'last_name':last_name, 'email':email})

@staff_member_required
def panelControl(request):
        return render(request, "content/panelControl.html",{})

def Contactar(request):
    message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            bd.crear_contactar(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                country=form.cleaned_data['country'],
                phone_number=form.cleaned_data['phone_number'],
                message=form.cleaned_data['message'],
                agree_to_policies=form.cleaned_data['agree_to_policies']
            )
            message = 'Tu mensaje ha sido enviado con exito!!'
            # form = ContactForm()
            return redirect('index')
        else:
            message = 'Error: Por favor, revisa los campos esten completos.'
    else:
        form = ContactForm()
    return render(request, 'content/Contactar.html', {'form': form, 'message': message})


@staff_member_required
def Incidencias(request):
        incidencias = bd.obtener_incidencias()
        return render(request, "content/incidencias.html",{'incidencias': incidencias})