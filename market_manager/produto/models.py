from django.db import models

# Create your models here.
class Produto(models.Model):
    name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=150)
    price = models.DecimalField(verbose_name='Preco', blank=False, null=False,max_digits=10,decimal_places=2)
    stock = models.IntegerField(verbose_name='Estoque', blank=False, null=False)
