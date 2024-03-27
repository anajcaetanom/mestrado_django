from django.shortcuts import render
from alunos.models import Aluno

# Create your views here.

def relatorioslist(request):
    return render(request, "relatorioslist.html") 

def relatorio_defesa(request):
    query = request.GET.get('q')
    if query:
        alunos_filtrados = Aluno.objects.filter(nome__icontains=query)
        defenderam = alunos_filtrados.filter(defesa=True).count()
        total_alunos = alunos_filtrados.count()
    else:
        alunos_filtrados = Aluno.objects.all()
        defenderam = alunos_filtrados.filter(defesa=True).count()
        total_alunos = alunos_filtrados.count()

    if total_alunos > 0:
        media = (defenderam / total_alunos) * 100
    else:
        media = 0

    return render(request, "relatorio_defesa.html", {'defenderam': defenderam, 'media': media, 'alunos': alunos_filtrados})


