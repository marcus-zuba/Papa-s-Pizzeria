from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

  def __init__(self, * args, ** kwargs):
    super(LoginForm, self).__init__( * args, ** kwargs)

  usuario = forms.CharField()
  senha = forms.CharField(widget=forms.PasswordInput)
