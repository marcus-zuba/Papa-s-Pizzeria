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
    carrinho = self.carrinho.copy()
    for key, item in carrinho.items():
      item['id'] = key
      item['produto'] = Produto.objects.get(id=item['produto_id'])
      item['preco'] = Decimal(item['preco'])
      item['preco_total'] = item['preco'] * item['quantidade']
      yield item

  def __len__(self):
    """
    Count all items in the cart.
    """
    return sum(item['quantidade'] for item in self.carrinho.values())

  def add(self, produto, quantidade=1, titulo="", preco=0):
    """
    Add a produto to the carrinho or atualizar its quantidade.
    """
    produto_id = str(produto.id)
    key_atual = None

    if(len(self.carrinho.keys())==0):
      proxima_key = '0'
    else:
      keys_ints = list(map(int, self.carrinho.keys()))
      proxima_key = str(max(keys_ints)+1)

    for key, value in self.carrinho.items():
      if produto_id == value['produto_id'] and produto_id != '-1':
        key_atual = key
      if produto_id == 1 and titulo == value['titulo']:
        key_atual = key

    if produto_id != '-1' and key_atual==None:
      self.carrinho[proxima_key] = {'titulo':produto.titulo, 
                                  'produto_id': produto_id,
                                  'quantidade': 0,
                                  'preco': str(produto.preco)}
    elif produto_id == '-1' and key_atual==None:
      self.carrinho[proxima_key] = {'titulo':titulo, 
                                  'produto_id': produto_id,
                                  'quantidade': 0,
                                  'preco': str(preco)}

    if key_atual == None:
      key_atual = proxima_key

    self.carrinho[key_atual]['quantidade'] += quantidade

    self.save()

  def update_quantidade(self, key, quantidade):
    self.carrinho[key]['quantidade'] = quantidade
    self.save()

  def remove(self, key):
    """
    Remove a produto from the cart.
    """
    if key in self.carrinho:
      del self.carrinho[key]
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
