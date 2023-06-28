from django import forms
from core.models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido','contraseña', 'edad', 'numero', 'foto', 'descripcion']

