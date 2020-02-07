from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from noticias.models import Articulo, Autor
from noticias.api.serializers import ArticuloSerializer, AutorSerializer 


class ArticuloListarCrearAPIView(APIView):

    def get(self, request):
        articulos = Articulo.objects.filter(activo=True)
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ArticuloDetalleAPIView(APIView):

    def get_object(self, pk):
        articulo =  get_object_or_404(Articulo, pk=pk)
        return articulo
    
    def get(self, request, pk):
        articulo = self.get_object(pk)
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data)

    def put(self, request, pk):
        articulo = self.get_object(pk)
        serializer = ArticuloSerializer(articulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        articulo = self.get_object(pk)
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AutorListarCrearAPIView(APIView):

    def get(self, request):
         autores = Autor.objects.all()
         serializer = AutorSerializer(autores, many=True, context={'request': request})
         return Response(serializer.data)

    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

"""
@api_view(["GET", "POST"])
def articulo_crear_api_view(request):
    if request.method == "GET":
        articulos = Articulo.objects.filter(activo=True)
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def articulo_detalle_api_view(request, pk):
    try:
        articulo = Articulo.objects.get(pk=pk)
    except Articulo.DoesNotExist:
        return Response({"error":{
                            "code": 404,
                            "message": "No existe el Articulo"
                        }}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET":
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ArticuloSerializer(articulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""