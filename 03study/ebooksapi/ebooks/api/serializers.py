from rest_framework import serializers
from ebooks.models import Ebook, Resena


class ResenaSerializer(serializers.ModelSerializer):

    autor_resena = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Resena
        exclude = ('ebook',)
        #  fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    resena = ResenaSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"