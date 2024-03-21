from django.shortcuts import render
from alunos.models import Aluno

# Create your views here.

def relatorioslist(request):
    defenderam = Aluno.objects.filter(defesa=True).count()
    aluno = Aluno.objects.all().values().count()
    media = f'{(defenderam/aluno)*100:.2f}'
    return render(request, "relatorioslist.html", {'defenderam' : defenderam, 'media' : media})

def buscar_produto(request):
    query = request.GET.get('q')
    if query:
        produtos = Aluno.objects.filter(nome__icontains=query)
    else:
        produtos = Aluno.objects.all()
    return render(request, 'teste.html', {'produtos': produtos})