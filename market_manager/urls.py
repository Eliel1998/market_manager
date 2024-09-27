from django.contrib import admin
from django.urls import path
from market_manager.home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('produtos/', views.produtos, name='listagem_produtos'),  
    path('produtos/<int:id>/', views.produto_detalhe, name='product_detail'),
    path('produtos/cadastro/', views.produto_cadastro, name='product_create'), 
    path('produtos/remover/<int:id>/', views.produto_remover, name='product_delete'),
    
    path('clientes/', views.clientes, name='listagem_clientes'),  
    path('clientes/<int:id>/', views.cliente_detalhe, name='client_detail'),
    path('clientes/cadastrar/', views.cliente_cadastro, name='client_create'),  
    path('clientes/remover/<int:id>/', views.cliente_remover, name='client_delete'),
    
    path('pedidos/', views.orders, name='order_list'), 
    path('pedidos/<int:id>/', views.order_detail, name='order_detail'),
    path('pedidos/cadastro/', views.pedido_cadastro, name='order_create'),
    path('pedidos/remover/<int:id>/', views.pedido_remover, name='order_delete'),
]
