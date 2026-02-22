from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, CategoriaViewSet

# O Router cria automaticamente as rotas: GET (lista), POST (cria), etc.
router = DefaultRouter()
router.register('produtos', ProdutoViewSet)
router.register('categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]