from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from noticias.models import Articulo, Autor


class ArticuloSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        exclude = ("id",)

    def get_time_since_publication(self, object):
        fecha_publicacion = object.fecha_publicacion
        ahora = datetime.now()
        time_delta = timesince(fecha_publicacion, ahora)
        return time_delta

    def validate(self, data):
        
        if data["titulo"] == data["descripcion"]:
            raise serializers.ValidationError("El titulo y la descripcion no pueden ser iguales")
        return data

    def validate_titulo(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("El titulo debe contener al menos 20 caracteres")
        return value


class AutorSerializer(serializers.ModelSerializer):

    articulos = serializers.HyperlinkedRelatedField(many=True,
                                                    read_only=True,
                                                    view_name="articulo-detalle")
    #articulos = ArticuloSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = "__all__"

"""
class ArticuloSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    autor = serializers.CharField()
    titulo = serializers.CharField()
    descripcion = serializers.CharField()
    contenido = serializers.CharField()
    lugar = serializers.CharField()
    fecha_publicacion = serializers.DateField()
    activo = serializers.BooleanField()
    creado = serializers.DateTimeField(read_only=True)
    actualizado = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Articulo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.autor = validated_data.get('autor', instance.autor)
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.descripcion = validated_data.get('descripcion', 
                                                    instance.descripcion)
        instance.contenido = validated_data.get('contenido', instance.contenido)
        instance.lugar = validated_data.get('lugar', instance.lugar)
        instance.fecha_publicacion = validated_data.get('fecha_publicacion',
                                                         instance.fecha_publicacion)
        instance.activo = validated_data.get('activo', instance.activo)
        instance.save()
        return instance

    def validate(self, data):
        
        if data["titulo"] == data["descripcion"]:
            raise serializers.ValidationError("El titulo y la descripcion no pueden ser iguales")
        return data

    def validate_titulo(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("El titulo debe contener al menos 20 caracteres")
        return value

"""