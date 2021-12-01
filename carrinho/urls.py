from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
  path('', views.carrinho_detalhado, name='carrinho_detalhado'),
  path('adicionar/<produto_id>/',views.cart_add,name='cart_add'),
  path('atualizar/<key>', views.cart_update, name='cart_update'),
  path('remover/<key>/',views.cart_remove,name='cart_remove'),
  path('limpar/', views.cart_clean, name='cart_clean')
]