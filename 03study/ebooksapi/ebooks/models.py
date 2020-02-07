from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Ebook(models.Model):
    titulo = models.CharField(max_length=140)
    autor = models.CharField(max_length=60)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo


class Resena(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    autor_resena = models.ForeignKey(User, on_delete=models.CASCADE)
    resena = models.TextField(blank=True, null=True)
    valoracion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name="Resena")

    def __str__(self):
        return str(self.valoracion)