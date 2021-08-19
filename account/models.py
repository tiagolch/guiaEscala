from django.contrib.auth.models import AbstractUser
from django.db import models

from ministerio.models import Funcao


class User(AbstractUser):
    funcao = models.ManyToManyField(Funcao)


