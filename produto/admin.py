from django.contrib import admin
from .models import Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'preco', 'categoria', 'disponivel']
  list_filter = ['categoria', 'disponivel']
  list_editable = ['preco', 'disponivel']
