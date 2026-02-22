from rest_framework import viewsets
from produtos.models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Interface para listar, criar e editar categorias via API.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Interface para listar, criar e editar produtos via API.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer