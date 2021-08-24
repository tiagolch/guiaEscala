from .models import Escala, Evento
from rest_framework import serializers


class EscalaSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()
    funcao = serializers.SerializerMethodField()
    evento = serializers.SerializerMethodField()
    class Meta:
        model = Escala
        fields = [
            'id',
            'nome',
            'datas',
            'funcao',
            'evento',
            'observacao'
        ]

    def get_nome(self, obj):
        return obj.__str__()

    def get_funcao(self, obj):
        return obj.get_funcao()

    def get_evento(self, obj):
        return obj.get_evento()


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = [
            'nome_evento',
            'getUltima_alteracao',
            'observacao'
        ]

