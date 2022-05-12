from django.db import models
from .User import User
# Create your models here.

class Address(models.Model):
  rua = models.CharField('rua',max_length=30)
  numero = models.BigIntegerField('numero')
  cep = models.BigIntegerField('cep')
  bairro = models.CharField('bairro',max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Rua: {self.rua}, Numero: {self.numero}, cep: {self.cep}, Bairro: {self.bairro}, Dono: {self.user.nome}" 