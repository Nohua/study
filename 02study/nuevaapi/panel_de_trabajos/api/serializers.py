from django.utils.timesince import timesince
from rest_framework import serializers
from panel_de_trabajos.models import OfertaLaboral


class OfertaLaboralSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfertaLaboral
        exclude = ("id",)

    def validate(self, data):
        
        if data["titulo_trabajo"] == data["descripcion_trabajo"]:
            raise serializers.ValidationError("El titulo y la descripcion no pueden ser iguales")
        return data

    def validate_titulo_trabajo(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("El titulo debe contener al menos 20 caracteres")
        return value
