from django import forms
from .models import Produto, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Eletrónicos, Ferramentas...'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Breve descrição da categoria (Opcional)'
            }),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        # Nota: O campo 'sku' foi removido porque o sistema gera-o automaticamente no Model
        fields = [
            'nome', 'categoria', 'preco_custo', 
            'preco_venda', 'quantidade_estoque', 'estoque_minimo'
        ]
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'preco_custo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'preco_venda': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
        }