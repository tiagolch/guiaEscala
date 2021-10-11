from django.contrib.auth.models import AbstractUser
from django.db import models

from ministerio.models import Funcao, Ministerio


class User(AbstractUser):
    ministerio = models.ForeignKey(Ministerio, on_delete=models.DO_NOTHING)
    funcao = models.ManyToManyField(Funcao)


