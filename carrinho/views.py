from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from produto.models import Produto, SaborPizza
from .carrinho import Carrinho
from .forms import CartAddProductForm, CartAddPizzaDoisSaboresForm
from decimal import Decimal
from django.utils.translation import gettext as _

# Create your views here.

@require_POST
def cart_add(request, produto_id):
  carrinho = Carrinho(request)
  if int(produto_id) != -1:
    produto = get_object_or_404(Produto, id=produto_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      carrinho.add(produto=produto,quantidade=cd['quantidade'])
  else:
    produto = get_object_or_404(Produto, id=produto_id)
    form = CartAddPizzaDoisSaboresForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      if(cd['primeiro_sabor']==cd['segundo_sabor']): 
        raise ValidationError(_('Os sabores devem ser diferentes!'), code='invalid')
      preco_sabor_1 = cd['primeiro_sabor'].preco
      preco_sabor_2 = cd['segundo_sabor'].preco
      preco = "{:.2f}".format(preco_sabor_1+preco_sabor_2/2)
      carrinho.add(produto=produto,quantidade=cd['quantidade'],
      titulo="Pizza de Dois Sabores: {} e {}".format(cd['primeiro_sabor'].sabor, cd['segundo_sabor'].sabor), preco=preco)
  return redirect('carrinho:carrinho_detalhado')

def cart_update(request, key):
  carrinho = Carrinho(request)
  form = CartAddProductForm(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    carrinho.update_quantidade(key, cd['quantidade'])

def cart_remove(request, key):
  carrinho = Carrinho(request)
  carrinho.remove(key)
  return redirect('carrinho:carrinho_detalhado')

def cart_clean(request):
  carrinho = Carrinho(request)
  carrinho.clear()
  return redirect('carrinho:carrinho_detalhado')

def carrinho_detalhado(request):
  carrinho = Carrinho(request)
  for item in carrinho:
    item['atualizar_quantidade_form'] = CartAddProductForm(
      initial={'quantidade': item['quantidade'],'update': True})

  return render(request, 'carrinho/carrinho_detalhado.html', {'carrinho': carrinho})