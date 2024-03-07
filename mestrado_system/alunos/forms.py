from django import forms
from .models import Aluno
from docentes.models import Docente

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
