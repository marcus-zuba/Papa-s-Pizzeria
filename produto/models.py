from django.db import models

# Create your models here.

class Produto(models.Model):

  OPCOES_CATEGORIAS = [
    ('SABOR', 'SABOR DE PIZZA'),
    ('BEBIDA', 'BEBIDA'),
    ('COMBO', 'COMBO')
  ]

  titulo = models.CharField(max_length=50)
  urlImagem = models.URLField(max_length=200)
  descricao = models.TextField(blank=True)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  categoria = models.CharField(max_length=6, choices=OPCOES_CATEGORIAS, default='SABOR')
  disponivel = models.BooleanField(default=True)