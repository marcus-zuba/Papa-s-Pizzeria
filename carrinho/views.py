from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from produto.models import Produto
from .carrinho import Carrinho
from .forms import CartAddProductForm

# Create your views here.

@require_POST
def cart_add(request, produto_id):
  carrinho = Carrinho(request)
  produto = get_object_or_404(Produto, id=produto_id)
  form = CartAddProductForm(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    carrinho.add(produto=produto,quantidade=cd['quantidade'],atualizar_quantidade=cd['update'])
  return redirect('carrinho:carrinho_detalhado')

def cart_remove(request, produto_id):
  carrinho = Carrinho(request)
  produto = get_object_or_404(Produto, id=produto_id)
  carrinho.remove(produto)
  return redirect('carrinho:carrinho_detalhado')

def carrinho_detalhado(request):
  carrinho = Carrinho(request)
  print(len(carrinho))
  return render(request, 'carrinho/carrinho_detalhado.html', {'carrinho': carrinho})