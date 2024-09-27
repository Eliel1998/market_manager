from django.db import models
from django.utils import timezone
from market_manager.cliente.models import Cliente
# Create your models here.
class Pedido(models.Model):
    date = models.DateTimeField(verbose_name='Data', blank=False, null=False, default= timezone.now)
    client = models.ForeignKey(Cliente, verbose_name='Cliente', blank=True, null=True, related_name='pedido_cliente', on_delete=models.CASCADE)
