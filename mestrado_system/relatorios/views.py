from django.shortcuts import render
from alunos.models import Aluno
from turmas.models import Turma


# Create your views here.

def relatorioslist(request):
    alunos = Aluno.objects.all()
    todas_as_turmas = Turma.objects.all().values()

    turmas_selecionadas_ids = request.GET.getlist('turmas')

    if turmas_selecionadas_ids:
        alunos = alunos.filter(turma__id__in=turmas_selecionadas_ids)

    return render(request, "relatorioslist.html", {'todas_as_turmas': todas_as_turmas})


def relatorio_defesa(request):
    query = request.GET.get('buscar_aluno')
    
    if query:
        alunos_filtrados = Aluno.objects.filter(nome__icontains=query)
        defenderam = alunos_filtrados.filter(defesa=True).count()
        total_alunos = alunos_filtrados.count()
    else:
        alunos_filtrados = Aluno.objects.all()
        defenderam = alunos_filtrados.filter(defesa=True).count()
        total_alunos = alunos_filtrados.count()

    if total_alunos > 0:
        porcentagem = (defenderam / total_alunos) * 100
    else:
        porcentagem = 0

    return render(request, "relatorio_defesa.html", {'alunos' : alunos,'defenderam': defenderam, 'porcentagem': porcentagem, 'alunos': alunos_filtrados})