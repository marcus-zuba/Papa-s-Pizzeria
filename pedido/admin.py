from django.contrib import admin
from .models import Pedido, ItemPedido

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
  pass

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
  pass
