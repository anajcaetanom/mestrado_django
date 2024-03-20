from django.shortcuts import render
from alunos.models import Aluno

# Create your views here.

def relatorioslist(request):
    return render(request, "relatorioslist.html")

def defesaQtd(request):
  contador = Aluno.objects.filter(defesa=True).count()
  return render(request, 'defesaCount.html', {'contador' : contador})