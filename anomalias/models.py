from django.db import models
from django.contrib.auth.models import User
from computadores.models import Computador


class Anomalia(models.Model):
    ESTADO_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_RESOLUCAO', 'Em Resolução'),
        ('RESOLVIDO', 'Resolvido'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    computador = models.ForeignKey(
        Computador, on_delete=models.CASCADE, related_name='anomalias')
    data_registo = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default='PENDENTE')
    reportado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
