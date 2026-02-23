from django.shortcuts import render, redirect
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm

# Tela 1: Dashboard (Alertas)
def dashboard_estoque(request):
    estoque_critico = Produto.objects.filter(quantidade_estoque__lt=10)
    context = {
        'produtos_alerta': estoque_critico,
        'total_geral': Produto.objects.count(),
        'em_estoque': Produto.objects.filter(quantidade_estoque__gt=0).count(),
        'alerta_count': estoque_critico.count(),
    }
    return render(request, 'dashboard.html', context)

# Tela 2: Listagem Geral (Todo o Inventário)
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('-criado_em')
    return render(request, 'listar_produtos.html', {'produtos': produtos})

# Tela 3: Cadastro de Produto (SKU Automático)
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos') # Redireciona para a lista após salvar
    else:
        form = ProdutoForm()
    return render(request, 'cadastro_produto.html', {'form': form})

# Tela 4: Cadastro de Categoria
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_produto')
    else:
        form = CategoriaForm()
    return render(request, 'cadastrar_categoria.html', {'form': form})