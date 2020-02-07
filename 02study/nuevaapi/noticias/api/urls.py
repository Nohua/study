from django.urls import path
from noticias.api.views import (
    ArticuloListarCrearAPIView, 
    ArticuloDetalleAPIView,
    AutorListarCrearAPIView,
)


urlpatterns =[
    path("articulo/", ArticuloListarCrearAPIView.as_view(), name="articulo-listar"),
    path("articulo/<int:pk>/", ArticuloDetalleAPIView.as_view(), name="articulo-detalle"),
    path("autor/", AutorListarCrearAPIView.as_view(), name="autor-listar"),
]