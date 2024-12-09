from django.db import models

# Create your models here.
class Marcas(models.Model):
    marca = models.CharField(max_length=50)
    def __str__(self):
        return self.marca
    
class Clases(models.TextChoices):
    AUTOMOVIL = 'a', 'automovil'
    BUS = 'b', 'bus'
    CAMION = 'c', 'camion'
    MOTO = 'm', 'moto'
    
    
class Automoviles(models.Model):
    placa = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    clase = models.CharField(max_length=1, choices=Clases.choices)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    electrico = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nit_ci = models.CharField(max_length=50)
    f_nacimiento = models.DateField()
    
class Cotizacion(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    automovil = models.ForeignKey(Automoviles, on_delete=models.CASCADE)
    valor_asegurado = models.DecimalField(max_digits=10, decimal_places=2)
    prima = models.DecimalField(max_digits=10, decimal_places=2)
    tasa = models.DecimalField(max_digits=10, decimal_places=2)