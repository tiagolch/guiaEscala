from .models import Ministerio, Funcao
from rest_framework import serializers


class MinisterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministerio
        fields = [
            'nome',
            'funcao',
            'ativo'
        ]


class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = [
            'funcao',
            'ativo'
        ]

