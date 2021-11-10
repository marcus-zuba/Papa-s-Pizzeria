from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def login_usuario(request):
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
          return HttpResponse('Autenticado '\
                              'com sucesso')
        else:
          return HttpResponse('Conta desativada')
      else:
        return HttpResponse('Login invalido')
  else:
    form = LoginForm()
  return render(request, 'conta/login.html', {'form': form})
