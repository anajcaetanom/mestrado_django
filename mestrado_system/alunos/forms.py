from django import forms
from .models import Aluno
from django.forms import DateInput

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'data_defesa': DateInput(attrs={
                'data-provide': 'datepicker',
                'class': 'form-control my-date-picker',
                'placeholder': 'DD/MM/YYYY',
            })
        }

class FiltroDataForm(forms.Form):
    data_inicio = forms.DateField(label='Data de início', required=False)
    data_fim = forms.DateField(label='Data de fim', required=False)