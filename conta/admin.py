from django.contrib import admin
from .models import Conta, Endereco, Bairro

# Register your models here.

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
  pass

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
  pass

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
  pass