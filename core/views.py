from django.shortcuts import render, redirect
from core.forms import RegistroForm
from .models import Usuario, Perfilt, Match, Chat

def login(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        
        # Lógica de validación del usuario y contraseña
        if nombre == 'nombre' and contraseña == 'contraseña':
            return redirect('perfil')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas.'})
    
    return render(request, 'login.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})


def dashboard(request):
    usuarios = Usuario.objects.all()
    return render(request, 'dashboard.html', {'usuarios': usuarios})


def perfil(request):
    perfil_usuario = Usuario.objects.get(usuario=request.user)
    return render(request, 'perfil.html', {'perfil_usuario': perfil_usuario})





def perfilt(request):
    nombre_user = Perfilt.objects.get(nombre_user=request.user)
    liked_users = Match.objects.filter(nombre_user=request.user, liked=True)
    return render(request, 'profile.html', {'user_profile': nombre_user, 'liked_users': liked_users})

def like_user(request, matched_user_id):
    matched_user = matched_user.objects.get(id=matched_user_id)
    Match.objects.create(user=request.user, matched_user=matched_user, liked=True)
    chat = Chat.objects.create(sender=request.user, receiver=matched_user, message="¡Hemos hecho match! Comencemos a chatear.")
    return redirect('chat', chat_id=chat.id)

def dislike_user(request, matched_user_id):
    matched_user = matched_user.objects.get(id=matched_user_id)
    Match.objects.create(matched_user=request.user, disliked=True)
    return redirect('perfil')

def chat(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    return render(request, 'chat.html', {'chat': chat})