from rest_framework import viewsets, filters 
from django_filters.rest_framework import DjangoFilterBackend
from produtos.models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    # Isso aqui conecta a View com as configurações do settings.py
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria'] 
    search_fields = ['nome', 'sku']

    @action(detail=False, methods=['get'])
    def estoque_baixo(self, request):
        """
        Retorna apenas os produtos com menos de 10 unidades.
        """
        produtos = Produto.objects.filter(quantidade__lt=10) # __lt significa 'Less Than' (Menor que)
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)
    

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer