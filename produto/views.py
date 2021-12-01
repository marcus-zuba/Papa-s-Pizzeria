from django.shortcuts import render

from .models import Produto
from carrinho.forms import CartAddProductForm, CartAddPizzaDoisSaboresForm

# Create your views here.

def cardapio(request):
  produtosAtivos = Produto.objects.filter(disponivel="True")
  sabores = produtosAtivos.filter(categoria="SABOR")
  bebidas = produtosAtivos.filter(categoria="BEBIDA")
  combos = produtosAtivos.filter(categoria="COMBO")

  carrinho_produto_form = CartAddProductForm()
  carrinho_dois_sabores_form = CartAddPizzaDoisSaboresForm()

  context = {
    'sabores' : sabores,
    'bebidas' : bebidas, 
    'combos' : combos,
    'form' : carrinho_produto_form,
    'form_dois_sabores': carrinho_dois_sabores_form
  }

  return render(request, "produto/cardapio.html", context)