from django.shortcuts import render
from .models import Produto

def dashboard_estoque(request):
    # Mudamos 'quantidade' para 'quantidade_estoque'
    estoque_critico = Produto.objects.filter(quantidade_estoque__lt=10)
    
    total_produtos = Produto.objects.count()
    # Mudamos aqui também para contar quem tem estoque
    produtos_ativos = Produto.objects.filter(quantidade_estoque__gt=0).count()
    
    context = {
        'produtos_alerta': estoque_critico,
        'total_geral': total_produtos,
        'em_estoque': produtos_ativos,
        'alerta_count': estoque_critico.count(),
    }
    return render(request, 'dashboard.html', context)