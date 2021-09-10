from django.db import models
from datetime import date

from account.models import User
from ministerio.models import Funcao


class Evento(models.Model):
    nome_evento = models.CharField(max_length=50, verbose_name='Evento')
    ultima_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    observacao = models.TextField(max_length=250, blank=True, null=True,)

    def __str__(self):
        return f'{self.nome_evento}'

    def getUltima_alteracao(self):
        return self.ultima_alteracao.strftime('%d/%m/%Y %H:%M')

    class Meta:
        verbose_name_plural = 'Eventos'


class Escala(models.Model):
    nome = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Responsavel')
    data = models.DateField(default=date.today())
    funcao = models.ForeignKey(Funcao, on_delete=models.DO_NOTHING, verbose_name='Função')
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING, verbose_name='Evento')
    observacao = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'

    def get_funcao(self):
        return f'{self.funcao}'

    def get_evento(self):
        return f'{self.evento}'

    def responsavel(self):
        return f'{self.nome.first_name} {self.nome.last_name}'

    def datas(self):
        return self.data.strftime('%d/%m/%Y')


