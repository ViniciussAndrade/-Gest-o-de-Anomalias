from django.urls import path
from . import views

app_name = 'anomalias'

urlpatterns = [
    path('', views.lista_anomalias, name='lista_anomalias'),
    path('registar/', views.registar_anomalia, name='registar_anomalia'),
    path('atualizar-estado/<int:pk>/', views.atualizar_estado, name='atualizar_estado'),
    path('relatorio/', views.relatorio_anomalias, name='relatorio_anomalias'),
]