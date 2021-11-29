from decimal import Decimal
from django.conf import settings
from produto.models import Produto
from conta.models import Endereco, Bairro

class Carrinho(object):
  def __init__(self, request):
    """
    Initialize the cart.
    """
    self.session = request.session
    carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
    if not carrinho:
      # save an empty carrinho in the session
      carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}
    self.carrinho = carrinho

    if request.user.is_authenticated:
      self.taxa_entrega = (Decimal)(Bairro.objects.get(pk=(
        Endereco.objects.get(usuario_id=request.user.id))
        .bairro_id).taxa_entrega)
    else:
      self.taxa_entrega = 0

  def __iter__(self):
    """
    Iterate over the items in the cart and get the products
    from the database.
    """
    produto_ids = self.carrinho.keys()
    # get the product objects and add them to the cart
    produtos = Produto.objects.filter(id__in=produto_ids)
    carrinho = self.carrinho.copy()
    for produto in produtos:
      carrinho[str(produto.id)]['produto'] = produto
      for item in carrinho.values():
        item['preco'] = Decimal(item['preco'])
        item['preco_total'] = item['preco'] * item['quantidade']
        yield item

  def __len__(self):
    """
    Count all items in the cart.
    """
    return sum(item['quantidade'] for item in self.carrinho.values())

  def add(self, produto, quantidade=1, atualizar_quantidade=False):
    """
    Add a produto to the carrinho or atualizar its quantidade.
    """
    produto_id = str(produto.id)
    if produto_id not in self.carrinho:
      self.carrinho[produto_id] = {'quantidade': 0,'preco': str(produto.preco)}
    if atualizar_quantidade:
      self.carrinho[produto_id]['quantidade'] = quantidade
    else:
      self.carrinho[produto_id]['quantidade'] += quantidade
    self.save()

  def remove(self, produto):
    """
    Remove a produto from the cart.
    """
    produto_id = str(produto.id)
    if produto_id in self.carrinho:
      del self.carrinho[produto_id]
    self.save()

  def save(self):
    # mark the session as "modified" to make sure it gets saved
    self.session.modified = True

  def get_taxa_entrega(self):
    return self.taxa_entrega

  def get_preco_total(self):
    return sum(Decimal(item['preco']) * item['quantidade'] for item in self.carrinho.values())

  def clear(self):
    # remove cart from session
    del self.session[settings.CARRINHO_SESSION_ID]
    self.save()
