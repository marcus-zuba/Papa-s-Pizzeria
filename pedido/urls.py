from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
  path('criar/', views.criar_pedido, name='criar_pedido'),
  path('detalhes/<pedido_id>/', views.pedido_detalhado, name='pedido_detalhado')
]
