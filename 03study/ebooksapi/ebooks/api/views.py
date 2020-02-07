from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from ebooks.models import Ebook, Resena
from ebooks.api.pagination import SmallSetPagination
from ebooks.api.serializers import EbookSerializer, ResenaSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsResenaAutorOrReadOnly


class EbookListCrearAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permissions_class = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permissions_class = [IsAdminUserOrReadOnly]


class ResenaCreateAPIView(generics.CreateAPIView): 
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    permissions_class = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        autor_resena = self.request.user

        resena_queryset = Resena.objects.filter(ebook=ebook,
                                                autor_resena=autor_resena)

        if resena_queryset.exists():
            raise ValidationError('Ya haz realizado una reseña ha este libro')

        serializer.save(ebook=ebook, autor_resena=autor_resena)


class ResenaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    permission_classes = [IsResenaAutorOrReadOnly]