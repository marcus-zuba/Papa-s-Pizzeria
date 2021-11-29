from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from cpf_field.models import CPFField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Bairro(models.Model):
  nome_bairro = models.CharField(max_length=50)
  taxa_entrega = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return '{}'.format(self.nome_bairro)

class Endereco(models.Model):
  usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  cep = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,10}$')])
  rua = models.CharField(max_length=50)
  bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
  numero = models.IntegerField()
  complemento = models.CharField(max_length=6, null=True)
  def __str__(self):
    return 'Endereço de CEP {} do usuário {}'.format(self.cep, self.usuario.username)


class Conta(models.Model):
  usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  nome_completo = models.CharField(max_length=100)
  cpf = CPFField('cpf')
  telefone = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])
  def __str__(self):
    return 'Conta do usuário {}'.format(self.usuario.username)

@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created:
      Conta.objects.create(usuario=instance, nome_completo="123", cpf="123", telefone="123")
      Endereco.objects.create(usuario=instance, cep="123", rua="123", bairro=Bairro.objects.get(pk=1), numero=123, complemento="")
      instance.conta.save()
      instance.endereco.save()

