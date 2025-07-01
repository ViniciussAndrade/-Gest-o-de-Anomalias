from django import forms
from .models import Anomalia
from salas.models import Sala


class AnomaliaForm(forms.ModelForm):
    class Meta:
        model = Anomalia
        fields = ['titulo', 'descricao', 'computador']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'computador': forms.Select(attrs={'class': 'form-control'}),
        }


class AnomaliaFilterForm(forms.Form):
    sala = forms.ModelChoiceField(
        queryset=Sala.objects.all(),
        required=False,
        empty_label="Todas as Salas",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    estado = forms.ChoiceField(
        choices=[('', 'Todos os Estados')] + Anomalia.ESTADO_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
