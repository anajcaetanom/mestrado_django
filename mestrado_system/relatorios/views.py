from django.shortcuts import render
from alunos.models import Aluno

# Create your views here.

def relatorioslist(request):
    return render(request, "relatorioslist.html") 

def relatorio_defesa(request):
    query = request.GET.get('q')
    if query:
        alunos = Aluno.objects.filter(nome__icontains=query)
    else:
        alunos = Aluno.objects.all()

    defenderam = Aluno.objects.filter(defesa=True).count()
    aluno = Aluno.objects.all().values().count()
    media = f'{(defenderam/aluno)*100:.2f}'
    return render(request, "relatorio_defesa.html", {'defenderam' : defenderam, 'media' : media, 'alunos': alunos})