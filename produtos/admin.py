from django.contrib import admin
from .models import Categoria, Produto, Movimentacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sku', 'quantidade_estoque', 'preco_venda')
    search_fields = ('nome', 'sku')
    list_filter = ('categoria',)

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data_hora')
    list_filter = ('tipo', 'data_hora')