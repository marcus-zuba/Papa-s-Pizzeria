from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms

urlpatterns = [
  # post views
  # path('login/', views.login_usuario, name='login'),
  path('', views.painel_usuario, name='painel_usuario'),
  path('cadastrar/', views.cadastrar_usuario, name='cadastrar'),
  path('login/', auth_views.LoginView.as_view(),name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('trocar_senha/',auth_views.PasswordChangeView.as_view(),name='trocar_senha'),
  path('trocar_senha/sucesso/',auth_views.PasswordChangeDoneView.as_view(),name='trocar_senha_sucesso'),
  path('redefinir_senha/',auth_views.PasswordResetView.as_view(),name='redefinir_senha'),
  path('redefinir_senha/sucesso/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
  path('redefinir/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='redefinir_senha_confirmacao'),
  path('redefinir/concluido/',auth_views.PasswordResetCompleteView.as_view(),name='redefinir_senha_concluido'),

]
