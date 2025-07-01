
from django import forms
from .models import Computador


class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = ['numero_identificacao', 'sala', 'marca',
                  'modelo', 'data_aquisicao', 'observacoes']
        widgets = {
            'data_aquisicao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'numero_identificacao': forms.TextInput(attrs={'class': 'form-control'}),
            'sala': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
        }
