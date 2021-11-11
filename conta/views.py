from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

from django.utils.translation import activate
    
# Create your views here.

def login_usuario(request):
  activate('pt-br')
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      usuario = authenticate(request,
                          username=cd['usuario'],
                          password=cd['senha'])
      if usuario is not None:
        if usuario.is_active:
          login(request, usuario)
  else:
    form = LoginForm()
  return render(request, 'conta/login.html', {'form': form})

@login_required
def painel_usuario(request):
  context = {'secao': 'painel_usuario'}
  return render(request, 'conta/painel_usuario.html', context)
