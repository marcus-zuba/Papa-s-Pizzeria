from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, ContaRegistrationForm, EnderecoRegistrationForm
from pedido.models import Pedido, ItemPedido
    
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
  else:
    form = LoginForm()
  return render(request, 'conta/login.html', {'form': form})

@login_required
def painel_usuario(request):
  compras = Pedido.objects.filter(usuario=request.user)
  return render(request, 'conta/painel_usuario.html', {'compras':compras})

"""
@login_required
def atualizar_login(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      

  form = UserRegistrationForm()
  string = "de Login"

@login_required
def atualizar_conta(request):
  form = ContaRegistrationForm()
  string = "Pessoais"

@login_required
def atualizar_endereco(request):
  form = EnderecoRegistrationForm()
  string = "de Endereço"
"""

def cadastrar_usuario(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    conta_form = ContaRegistrationForm(request.POST)
    endereco_form = EnderecoRegistrationForm(request.POST)
    if user_form.is_valid() and conta_form.is_valid() and endereco_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password'])
      # Save the User object
      new_user.save()
      new_user.refresh_from_db()
      conta_form = ContaRegistrationForm(request.POST, instance=new_user.conta)
      conta_form.full_clean()
      conta_form.save()
      endereco_form = EnderecoRegistrationForm(request.POST, instance=new_user.endereco)
      endereco_form.full_clean()
      endereco_form.save()
      return render(request,'conta/cadastro_completo.html',{'new_user': new_user})
#      return render(request,'registrado',{'new_user': new_user})
  else:
    user_form = UserRegistrationForm()
    conta_form = ContaRegistrationForm()
    endereco_form = EnderecoRegistrationForm()
  return render(request,'conta/cadastro.html',
    {'user_form': user_form, 
      'conta_form': conta_form,
      'endereco_form': endereco_form})
