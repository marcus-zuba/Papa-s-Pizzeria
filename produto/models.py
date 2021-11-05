from django.db import models

# Create your models here.

class Produto(models.Model):
  titulo = models.CharField(max_length=50)
  urlImagem = models.URLField(max_length=200)
  descricao = models.TextField(blank=True)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  disponivel = models.BooleanField(default=True)
  criado = models.DateTimeField(auto_now_add=True)
  atualizado = models.DateTimeField(auto_now=True)