from django.db import models


class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=6, verbose_name='id ususario')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    numero = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos/')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Mensaje(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)