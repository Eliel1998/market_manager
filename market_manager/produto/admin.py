from django.contrib import admin
from market_manager.produto.models import Produto
# Register your models here.

@admin.register(Produto)
class AdminProduto(admin.ModelAdmin):
    model : Produto
    fields = ('name','price','stock')
    readonly_fields = ['id']
