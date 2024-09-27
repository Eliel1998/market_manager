from django.contrib import admin
from market_manager.pedido_produto.models import PedidoProduto
# Register your models here.
@admin.register(PedidoProduto)
class AdminPedidoProduto(admin.ModelAdmin):
    model = PedidoProduto
    fields = ('order','product','quantity')
    readonly_fields = ['id']
