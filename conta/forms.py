from django import forms

class LoginForm(forms.Form):
  usuario = forms.CharField()
  senha = forms.CharField(widget=forms.PasswordInput)
