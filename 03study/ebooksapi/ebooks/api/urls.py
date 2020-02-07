from django.urls import path
from ebooks.api.views import EbookListCrearAPIView, EbookDetailAPIView, ResenaCreateAPIView, ResenaDetailAPIView

urlpatterns = [
        path('ebooks/', EbookListCrearAPIView.as_view(), name='ebook-list'),
        path('ebooks/<int:pk>', EbookDetailAPIView.as_view(), name='ebook-detail'),
        path('ebooks/<int:ebook_pk>/resena', ResenaCreateAPIView.as_view(), name='ebook-resena'),
        path('resena/<int:pk>', ResenaDetailAPIView.as_view(), name='resena-detail'),
]