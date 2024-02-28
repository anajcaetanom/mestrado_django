from django import forms
from .models import Turma

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'vagas', 'curso', 'data_de_inicio']
        widgets = {
            'data_de_inicio': forms.DateInput(attrs={'type': 'date'}),
        }