from django.contrib import admin
from django.urls import path
from produtos.views import (
    dashboard_estoque, 
    cadastrar_produto, 
    cadastrar_categoria, # Certifique-se de importar a view
    listar_produtos
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_estoque, name='dashboard'),
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/novo/', cadastrar_produto, name='cadastrar_produto'),
    
    # ESTA É A LINHA QUE ESTÁ FALTANDO OU ESTÁ COM O NOME ERRADO:
    path('categorias/novo/', cadastrar_categoria, name='cadastrar_categoria'),
]