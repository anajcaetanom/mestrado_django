from django import forms
from .models import Aluno
from django.forms import DateInput

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            "nome", 
            "sobrenome", 
            "curso", 
            "orientadores", 
            "defesa", 
            "data_defesa", 
            "artigo", 
            "bolsista",
            "obs", 
            "email", 
            "matricula"
            ]
        ets = {
            'data_defesa': DateInput(attrs={
                'data-provide': 'datepicker',
                'class': 'form-control my-date-picker',
                'placeholder': 'DD/MM/YYYY',
            })
        }

class AlunoForm_Edit(AlunoForm):

    class Meta(AlunoForm.Meta):
        fields = AlunoForm.Meta.fields + ['situacao', 'motivo']

class AlunoForm_Situacao(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['motivo']


class FiltroDataForm(forms.Form):
    data_inicio = forms.DateField(label='Data de início', required=False)
    data_fim = forms.DateField(label='Data de fim', required=False)