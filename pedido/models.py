from django.db import models
from django.conf import settings
from produto.models import Produto

# Create your models here.

class Pedido(models.Model):
  usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  taxa_entrega = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  criado = models.DateTimeField(auto_now_add=True)
  atualizado = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('-criado',)

  def __str__(self):
    return 'Pedido {}'.format(self.id)
 
  def get_total_cost(self):
    return sum(item.get_cost() for item in self.items.all()) + self.taxa_entrega

class ItemPedido(models.Model):
  pedido = models.ForeignKey(Pedido,related_name='items',on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto,related_name='pedido_items',on_delete=models.CASCADE)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  quantidade = models.PositiveIntegerField(default=1)
  descricao = models.CharField(max_length=100,default='')
  def __str__(self):
    return '{}'.format(self.id)
  def get_cost(self):
    return self.preco * self.quantidade