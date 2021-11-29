from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, ItemPedido
from carrinho.carrinho import Carrinho

# Create your views here.

@login_required
def criar_pedido(request):
  carrinho = Carrinho(request)
  if request.method == 'POST':
    pedido = Pedido.objects.create(usuario=request.user, taxa_entrega=carrinho.taxa_entrega)
    for item in carrinho:
      ItemPedido.objects.create(pedido=pedido, produto=item['produto'], 
      preco=item['preco'], quantidade=item['quantidade'])
    carrinho.clear()
    return render(request,'pedido/pedido_concluido.html',{'pedido': pedido})
  else:
    return redirect('carrinho:carrinho_detalhado')
