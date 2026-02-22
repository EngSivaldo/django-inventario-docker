from rest_framework import serializers
from produtos.models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__' # Exporta todos os campos da categoria

class ProdutoSerializer(serializers.ModelSerializer):
    # Mostra o nome da categoria em vez de apenas o ID (mais legível)
    categoria_nome = serializers.ReadOnlyField(source='categoria.nome')

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'sku', 'categoria', 'categoria_nome', 
            'preco_venda', 'quantidade_estoque', 'estoque_minimo'
        ]