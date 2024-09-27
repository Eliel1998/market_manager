from django.contrib import admin
from market_manager.cliente.models import Cliente
# Register your models here.
@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    model = Cliente
    fields = ('email','name')
    readonly_fields = ['id']
