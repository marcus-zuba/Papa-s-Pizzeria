from django.shortcuts import render

from .models import Produto
from carrinho.forms import CartAddProductForm

# Create your views here.

def cardapio(request):
  produtosAtivos = Produto.objects.filter(disponivel="True")
  sabores = produtosAtivos.filter(categoria="SABOR")
  bebidas = produtosAtivos.filter(categoria="BEBIDA")
  combos = produtosAtivos.filter(categoria="COMBO")

  carrinho_produto_form = CartAddProductForm()

  context = {
    'sabores' : sabores,
    'bebidas' : bebidas, 
    'combos' : combos,
    'form' : carrinho_produto_form
  }

  return render(request, "produto/cardapio.html", context)