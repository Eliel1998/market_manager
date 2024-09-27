from django.db import models
from market_manager.pedido.models import Pedido
from market_manager.produto.models import Produto
# Create your models here.
class PedidoProduto(models.Model):
    order = models.ForeignKey(Pedido, verbose_name='Pedido', blank=True, null=True,related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Produto, verbose_name='Produto', blank=True, null=True, related_name='pedido_produto', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Quantidade', blank=False, null=False)