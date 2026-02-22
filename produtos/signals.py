from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movimentacao

@receiver(post_save, sender=Movimentacao)
def atualizar_estoque(sender, instance, created, **kwargs):
    """
    Gatilho que dispara sempre que uma nova Movimentação é salva.
    """
    if created:
        produto = instance.produto
        if instance.tipo == 'E':  # 'E' de Entrada
            produto.quantidade_estoque += instance.quantidade
        elif instance.tipo == 'S':  # 'S' de Saída
            produto.quantidade_estoque -= instance.quantidade
        
        produto.save()