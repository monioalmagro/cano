from django.db import models


class Lista(models.Model):
    marca = models.CharField(max_length=50, verbose_name= "Marca")
    producto = models.CharField(max_length=50,verbose_name= "Producto")
    peso = models.CharField(max_length=100)
    masdecuatrounidades = models.DecimalField(max_digits=5, decimal_places=2)
    porHorma = models.DecimalField(max_digits=5, decimal_places=2)
    fraccionado = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificación")
    

    class Meta:
        verbose_name ="lista"
        verbose_name_plural ="listas"

    def __str__(self):
        return self.marca
