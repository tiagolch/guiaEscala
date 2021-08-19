from django.db import models


class Funcao(models.Model):
    funcao = models.CharField(max_length=50, verbose_name='Função')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.funcao}'

    class Meta:
        verbose_name_plural = 'Funcoes'


class Ministerio(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Ministério')
    funcao = models.ManyToManyField(Funcao, verbose_name='Função')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def get_funcao(self):
        return f'{self.funcao}'

    class Meta:
        verbose_name_plural = 'Ministerios'


