from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from conta.models import Conta, Endereco, Bairro

class LoginForm(AuthenticationForm):

  def __init__(self, * args, ** kwargs):
    super(LoginForm, self).__init__( * args, ** kwargs)

  usuario = forms.CharField()
  senha = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
  username = forms.CharField(label='Usuario')
  email = forms.EmailField(label='Email')
  password = forms.CharField(label='Senha',widget=forms.PasswordInput)
  password2 = forms.CharField(label='Repita sua senha',widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ('username', 'email',)
  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']

class UserUpdateForm(forms.ModelForm):
  username = forms.CharField(label='Usuario')
  email = forms.EmailField(label='Email')
  class Meta:
    model = User
    fields = ('username', 'email',)

class ContaRegistrationForm(forms.ModelForm):
  class Meta:
    model = Conta
    fields = ('nome_completo', 'cpf', 'telefone')

class EnderecoRegistrationForm(forms.ModelForm):
  bairro = forms.ModelChoiceField(queryset=Bairro.objects.all(), initial=0)
  class Meta:
    model = Endereco
    fields = ('cep', 'rua', 'bairro', 'numero', 'complemento')
