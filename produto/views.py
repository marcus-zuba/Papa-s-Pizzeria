from django.shortcuts import render

from .models import Produto

# Create your views here.

def produto_detalhado_view(request):
  obj = Produto.objects.get(id=1)

  context = { 'object':obj }

  return render(request, "produto/produto_detalhado.html", context)
