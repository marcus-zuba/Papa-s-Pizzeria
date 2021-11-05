from django.shortcuts import render

from .models import Produto

# Create your views here.

def cardapio(request):
  produtosAtivos = Produto.objects.filter(disponivel="True")
  sabores = produtosAtivos.filter(categoria="SABOR")
  bebidas = produtosAtivos.filter(categoria="BEBIDA")
  combos = produtosAtivos.filter(categoria="COMBO")

  context = {
    'sabores' : sabores,
    'bebidas' : bebidas, 
    'combos' : combos
  }

  return render(request, "produto/cardapio.html", context)