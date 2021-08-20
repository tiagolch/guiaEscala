from .models import Escala, Evento
from rest_framework import serializers


class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = "__all__"


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"

