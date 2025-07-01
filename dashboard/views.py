from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from salas.models import Sala
from computadores.models import Computador
from anomalias.models import Anomalia


def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def dashboard(request):
    # Estatísticas gerais
    total_salas = Sala.objects.count()
    total_computadores = Computador.objects.count()
    total_anomalias = Anomalia.objects.count()

    # Anomalias por estado
    anomalias_por_estado = Anomalia.objects.values(
        'estado').annotate(total=Count('id'))

    # Anomalias recentes (últimos 7 dias)
    data_limite = timezone.now() - timedelta(days=7)
    anomalias_recentes = Anomalia.objects.filter(
        data_registo__gte=data_limite
    ).order_by('-data_registo')[:5]

    # Salas com mais anomalias
    salas_problematicas = Sala.objects.annotate(
        num_anomalias=Count('computadores__anomalias')
    ).order_by('-num_anomalias')[:5]

    # Computadores com mais anomalias
    computadores_problematicos = Computador.objects.annotate(
        num_anomalias=Count('anomalias')
    ).order_by('-num_anomalias')[:5]

    context = {
        'total_salas': total_salas,
        'total_computadores': total_computadores,
        'total_anomalias': total_anomalias,
        'anomalias_por_estado': anomalias_por_estado,
        'anomalias_recentes': anomalias_recentes,
        'salas_problematicas': salas_problematicas,
        'computadores_problematicos': computadores_problematicos,
    }

    return render(request, 'dashboard/index.html', context)
