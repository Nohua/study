from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return f"{ self.nombre} {self.apellidos}"  


class Articulo(models.Model):
    autor = models.ForeignKey(Autor, related_name="articulos", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=200)
    contenido = models.TextField()
    lugar = models.CharField(max_length=120)
    fecha_publicacion = models.DateField()
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.autor} {self.titulo}"
