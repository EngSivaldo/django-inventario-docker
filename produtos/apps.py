from django.apps import AppConfig

class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'

    def ready(self):
        import produtos.signals  # Isso carrega o vigia quando o sistema liga