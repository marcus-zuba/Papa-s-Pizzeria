from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
  path('', views.carrinho_detalhado, name='carrinho_detalhado'),
  path('adicionar/<int:produto_id>/',views.cart_add,name='cart_add'),
  path('remover/<int:produto_id>/',views.cart_remove,name='cart_remove'),
]