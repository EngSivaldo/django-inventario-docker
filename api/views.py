from rest_framework import viewsets, filters 
from django_filters.rest_framework import DjangoFilterBackend
from produtos.models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    # Isso aqui conecta a View com as configurações do settings.py
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria', 'ativo'] 
    search_fields = ['nome', 'sku']

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer