from django.contrib import admin
from .models import Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'preco', 'disponivel', 
                  'criado', 'atualizado']
  list_filter = ['disponivel','criado', 'atualizado']
  list_editable = ['preco', 'disponivel']
