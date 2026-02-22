from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    CARGO_CHOICES = (
        ('G', 'Gerente'),
        ('O', 'Operador'),
    )
    cargo = models.CharField(max_length=1, choices=CARGO_CHOICES, default='O')
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_cargo_display()}"