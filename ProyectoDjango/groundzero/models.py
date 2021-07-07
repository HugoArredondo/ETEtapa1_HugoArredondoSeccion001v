from django.db import models

# Create your models here.
class Proveedor(models.Model):
    numIdenti = models.IntegerField(primary_key=True, verbose_name='Número de Identificación')
    photo = models.ImageField(verbose_name='Fotografía')
    nombreProveedor = models.CharField(max_length=200, verbose_name='Nombre Completo')
    numContactoProveedor = models.IntegerField(verbose_name='Número de Contacto (+569)')
    direccionProveedor = models.CharField(max_length=150, verbose_name='Dirección')
    correoProveedor = models.CharField(max_length=100, verbose_name='Correo Electrónico')
    paisProveedor = models.CharField(max_length=50, verbose_name='País')
    contraseña = models.CharField(max_length=10, verbose_name='Contraseña')
    monedaPago = models.CharField(max_length=5, verbose_name='Moneda de Pago')
    
    def __str__(self):
        return self.nombreProveedor