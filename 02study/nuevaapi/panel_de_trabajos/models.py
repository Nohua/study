from django.db import models


MONEDAS_CHOICES = [
    ('USD', 'Dólares'),
    ('CLP', 'Peso Chileno'),
    ('EUR', 'Euro'),
    ('CNY', 'Yuan chino'),
    ('CAD', 'Dólar canadiense'),
    ('JPY', 'Yen'),
    ('GBP', 'Libra esterlina'),
    ('RUB', 'Rublo ruso'),
]

class OfertaLaboral(models.Model):
    nombre_empresa = models.CharField(max_length=60)
    email_empresa = models.EmailField()
    titulo_trabajo = models.CharField(max_length=120)
    descripcion_trabajo = models.TextField()
    salario = models.IntegerField()
    ciudad = models.CharField(max_length=30)
    estado = models.BooleanField(default=True, verbose_name="Activo")
    moneda = models.CharField(max_length=3,default=None, choices=MONEDAS_CHOICES)
    
    def __str__(self):
        return f"{self.nombre_empresa} {'-'} {self.titulo_trabajo}"