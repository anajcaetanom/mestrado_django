from django import forms
from .models import Turma

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'vagas', 'curso', 'data_de_inicio']