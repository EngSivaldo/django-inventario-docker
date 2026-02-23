
from django.contrib import admin
from django.urls import path, include

from produtos.views import dashboard_estoque

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # Conecta as rotas 
    path('dashboard/', dashboard_estoque, name='dashboard'),
]
