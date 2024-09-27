from django.shortcuts import get_object_or_404, redirect, render
from market_manager.cliente.models import Cliente
from market_manager.pedido.models import Pedido
from market_manager.pedido_produto.models import PedidoProduto
from market_manager.produto.models import Produto
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from enum import Enum

class HttpMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

def home(request):
    return render(request, 'home/home.html')


# [feature de produtos]
@csrf_exempt
def produtos(request):
    if request.headers.get('Accept') == 'application/json':
        produtos = list(Produto.objects.values())
        return JsonResponse({'produtos': produtos}, safe=False)
    else:
        produtos = {
            'produtos': Produto.objects.all()
        }
        return render(request, 'home/product/product_list.html', produtos)

def produto_detalhe(request, id):
    produto = {
        'produto' : Produto.objects.get(id=id),
    }
    return render(request, 'home/product/product_detail.html', produto)

@csrf_exempt
def produto_cadastro(request):

    if request.method == HttpMethod.POST.value:
        return produto_salvar(request)
    
    return render(request, 'home/product/product_create.html')

def produto_salvar(request):
    novo_produto = Produto()
    if request.method == HttpMethod.POST.value:
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                novo_produto.name = data.get('name')
                novo_produto.price = data.get('price')
                novo_produto.stock = data.get('stock')
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Dados JSON inválidos'}, status=400)
        else:
            novo_produto.name = request.POST.get('name')
            novo_produto.price = request.POST.get('price')
            novo_produto.stock = request.POST.get('stock')

        if not novo_produto.name or not novo_produto.price or not novo_produto.stock:
            return JsonResponse({'error': 'Nome, preço e estoque são obrigatórios'}, status=400)
        
    novo_produto.save()
    return produtos(request)

@csrf_exempt
def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == HttpMethod.POST.value:
        produto.delete()
        return redirect('listagem_produtos')
    
    elif request.method == HttpMethod.DELETE.value:
        produto.delete()
        return JsonResponse({'message': 'Produto removido com sucesso'}, status=200)
    
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

# [feature de clientes]

@csrf_exempt
def clientes(request):
    if request.headers.get('Accept') == 'application/json':
        clientes = list(Cliente.objects.values())
        return JsonResponse({'clientes': clientes}, safe=False)
    else:
        clientes = {
            'clientes' : Cliente.objects.all()
        }
    return render(request, 'home/client/client_list.html', clientes)

def cliente_detalhe(request, id):
    cliente = {
        'cliente' : Cliente.objects.get(id=id)
    }
    return render(request, 'home/client/client_detail.html', cliente)

@csrf_exempt
def cliente_cadastro(request):
    if request.method == HttpMethod.POST.value:
        return cliente_salvar(request)
    
    return render(request, 'home/client/client_create.html')

@csrf_exempt
def cliente_salvar(request):
    if request.method == HttpMethod.POST.value:
        novo_cliente = Cliente()
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                novo_cliente.name = data.get('name')
                novo_cliente.email = data.get('email')
                
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Dados JSON inválidos'}, status=400)
        else:
            novo_cliente.name = request.POST.get('name')
            novo_cliente.email = request.POST.get('email')

        if not novo_cliente.name or not novo_cliente.email:
            return JsonResponse({'error': 'Nome e email são obrigatórios'}, status=400)

        novo_cliente.save()
        return clientes(request)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
@csrf_exempt
def cliente_remover(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == HttpMethod.POST.value:
        cliente.delete()
        return redirect('listagem_clientes')
    
    elif request.method == HttpMethod.DELETE.value:
        cliente.delete()
        return JsonResponse({'message': 'Cliente removido com sucesso'}, status=200)
    
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    
# [feature de pedidos]
@csrf_exempt
def orders(request):
    if request.headers.get('Accept') == 'application/json':
        orders = list(Pedido.objects.values())
        return JsonResponse({'orders': orders}, safe=False)
    else:
        orders = {
            'orders' : Pedido.objects.all()
        }
    return render(request, 'home/order/order_list.html', orders)


@csrf_exempt
def pedido_cadastro(request):
    novo_pedido = Pedido()
    pedido_produto = PedidoProduto()

    if request.method == HttpMethod.POST.value:
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                novo_pedido.date = data.get('data')
                cliente_id = data.get('cliente')
                produto_id = data.get('produto')
                pedido_produto.quantity = data.get('quantidade')

                if not verify_client_exist(cliente_id):
                    return JsonResponse({'error': 'Cliente não encontrado'}, status=404)
                
                if not verifify_product_exist_and_stock(produto_id, pedido_produto.quantity):
                    return JsonResponse({'error': 'Produto não encontrado ou estoque insuficiente'}, status=404)

            except json.JSONDecodeError:
                return JsonResponse({'error': 'Dados JSON inválidos'}, status=400)
            
        else:
            novo_pedido.date = request.POST.get('data')
            cliente_id = request.POST.get('cliente')
            produto_id = request.POST.get('produto')
            pedido_produto.quantity = request.POST.get('quantidade')
        
        novo_pedido.client = get_object_or_404(Cliente, id=cliente_id)
        novo_pedido.save()

        pedido_produto.order = novo_pedido
        pedido_produto.product = get_object_or_404(Produto, id=produto_id)
        pedido_produto.save()

        return redirect('order_list') 
    
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'home/order/order_create.html', {'clientes': clientes, 'produtos': produtos})

def order_detail(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido_produto = PedidoProduto.objects.filter(order=pedido)
    products = Produto.objects.all()

    order = {
        'order' : pedido,
        'pedido_produto' : pedido_produto,
        'products' : products
    }
    
    return render(request, 'home/order/order_detail.html', order)

@csrf_exempt
def pedido_remover(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    
    if request.method == HttpMethod.POST.value:
        pedido.delete()
        return redirect('order_list')
    
    elif request.method == HttpMethod.DELETE.value:
        pedido.delete()
        return JsonResponse({'message': 'Pedido removido com sucesso'}, status=200)
    
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
def verify_client_exist(cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        return True
    except Cliente.DoesNotExist:
        return False
    
def verifify_product_exist_and_stock(produto_id, quantidade):
    try:
        produto = Produto.objects.get(id=produto_id)
        if produto.stock < quantidade:
            return False
        return True
    except Produto.DoesNotExist:
        return False
