from django.urls import path
from panel_de_trabajos.api.views import (
    OfertaLaboralListarCrearAPIView,
    OfertaLaboralDetalleAPIView
)


urlpatterns =[
    path("ofertalaboral/", OfertaLaboralListarCrearAPIView.as_view(), name="oferta-listar"),
    path("ofertalaboral/<int:pk>/", OfertaLaboralDetalleAPIView.as_view(), name="oferta-detalle"),

]