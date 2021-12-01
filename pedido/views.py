from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Pedido, ItemPedido
from carrinho.carrinho import Carrinho

# Create your views here.

@login_required
@require_POST
def criar_pedido(request):
  carrinho = Carrinho(request)
  if request.method == 'POST':
    if len(carrinho)>0:
      pedido = Pedido.objects.create(usuario=request.user, taxa_entrega=carrinho.taxa_entrega)
      for item in carrinho:
          ItemPedido.objects.create(pedido=pedido, produto=item['produto'], 
          preco=item['preco'], quantidade=item['quantidade'], descricao=item['titulo'])
      carrinho.clear()
      return render(request,'pedido/pedido_concluido.html',{'pedido': pedido})
    else:
      return redirect('cardapio')

def pedido_detalhado(request, pedido_id):
  pedido = Pedido.objects.get(id=pedido_id)
  return render(request, 'pedido/pedido_detalhado.html',{'pedido':pedido})
