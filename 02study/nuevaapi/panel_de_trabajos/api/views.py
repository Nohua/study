from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from panel_de_trabajos.models import OfertaLaboral
from panel_de_trabajos.api.serializers import OfertaLaboralSerializer


class OfertaLaboralListarCrearAPIView(APIView):

    def get(self, request):
        ofertas = OfertaLaboral.objects.filter(estado=True)
        serializer = OfertaLaboralSerializer(ofertas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OfertaLaboralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OfertaLaboralDetalleAPIView(APIView):

    def get_object(self, pk):
        oferta =  get_object_or_404(OfertaLaboral, pk=pk)
        return oferta
    
    def get(self, request, pk):
        oferta = self.get_object(pk)
        serializer = OfertaLaboralSerializer(oferta)
        return Response(serializer.data)

    def put(self, request, pk):
        oferta = self.get_object(pk)
        serializer = OfertaLaboralSerializer(oferta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        oferta = self.get_object(pk)
        oferta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)