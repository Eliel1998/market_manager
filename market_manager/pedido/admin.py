from django.contrib import admin
from market_manager.pedido.models import Pedido
# Register your models here.
@admin.register(Pedido)
class AdminPedido(admin.ModelAdmin):
    model = Pedido
    fields = ['client']
    readonly_fields = ['date']
