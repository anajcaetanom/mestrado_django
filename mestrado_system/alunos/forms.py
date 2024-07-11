from django import forms
from .models import Aluno
from django.forms import DateInput

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            "nome", 
            "sobrenome", 
            "turma", 
            "orientadores", 
            "defesa", 
            "data_defesa", 
            "artigo", 
            "eh_bolsista",
            "nome_da_bolsa",
            "obs", 
            "email", 
            "matricula",
            "academico"
        ]
        widgets = {
            'data_defesa': DateInput(attrs={
                'data-provide': 'datepicker',
                'class': 'form-control my-date-picker',
                'placeholder': 'DD/MM/YYYY',
            })
        }

class AlunoForm_Edit(AlunoForm):
    
    class Meta(AlunoForm.Meta):
        fields = AlunoForm.Meta.fields + ['situacao', 'motivo']