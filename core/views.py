from django.shortcuts import render, redirect
from core.models import Usuario
from core.forms import RegistroForm
from .models import Mensaje

def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        
        # Lógica de validación del usuario y contraseña
        if nombre == 'nombre' and contraseña == 'contraseña':
            return redirect('perfil_view')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas.'})
    
    return render(request, 'login.html')


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})


def dashboard_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'dashboard.html', {'usuarios': usuarios})


def perfil_view(request):
    perfil_usuario = Usuario.objects.get(usuario=request.user)
    return render(request, 'perfil.html', {'perfil_usuario': perfil_usuario})





def chat(request):
    mensajes = Mensaje.objects.all().order_by('fecha')
    return render(request, 'chat.html', {'mensajes': mensajes})

def enviar_mensaje(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        mensaje = Mensaje(contenido=contenido)
        mensaje.save()
    return redirect('chat')