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
    


class Perfilt(models.Model):
    nombre_user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    apellido_user = models.CharField(max_length=100)
    edad_user = models.PositiveIntegerField()
    foto_user = models.ImageField(upload_to='fotos/')
    descripcion_user = models.TextField()



class Match(models.Model):
    nombre_user1 = models.ForeignKey(Perfilt, on_delete=models.CASCADE, related_name='matches')
    matched_user = models.ForeignKey(Perfilt, on_delete=models.CASCADE, related_name='matched_by')
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)


class Chat(models.Model):
    remitente = models.ForeignKey(Perfilt, on_delete=models.CASCADE, related_name='enviado')
    receptor = models.ForeignKey(Perfilt, on_delete=models.CASCADE, related_name='recibido')
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
