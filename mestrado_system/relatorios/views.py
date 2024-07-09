from django.shortcuts import render
from alunos.models import Aluno
from turmas.models import Turma
from docentes.models import Docente
from django.contrib import messages


# Create your views here.

def relatorioslist(request):
    alunos = Aluno.objects.all()
    todas_as_turmas = Turma.objects.all().values().order_by('nome')
    todos_os_docentes = Docente.objects.all().values().order_by('nome')

    turmas_selecionadas_ids = request.GET.getlist('turmas')

    if turmas_selecionadas_ids:
        alunos = alunos.filter(turma__id__in=turmas_selecionadas_ids)

    return render(request, "relatorioslist.html", {'todas_as_turmas': todas_as_turmas, 'todos_os_docentes': todos_os_docentes})


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

def filtrar_alunos(request):
    turma_selecionada = request.GET.get('turma')
    ano = request.GET.get('ano')
    docente_selecionado = request.GET.get('docente')
    situacao_selecionada = request.GET.get('situacao_all')

    alunos = Aluno.objects.all().order_by('situacao')
    turmas = Turma.objects.all()
    docentes = Docente.objects.all()
    situacao_all = Aluno.SITUACAO_CHOICES

    if turma_selecionada:
        alunos = alunos.filter(turma__id=turma_selecionada)

    if ano:
        try:
            ano = int(ano)
            if 3000 > ano > 1900:
                alunos = alunos.filter(data_defesa__year=ano)
            else:
                messages.error(request, 'Por favor, insira um ano válido.')
        except ValueError:
            messages.error(request, 'Por favor, insira um ano válido.')

    if docente_selecionado:
        alunos = alunos.filter(orientadores__id=docente_selecionado)

    if situacao_selecionada:
        alunos = alunos.filter(situacao=situacao_selecionada)

    alunos_count = alunos.count()

    contexto = {
        'alunos': alunos,
        'turmas': turmas,
        'docentes': docentes,
        'turma_selecionada': turma_selecionada,
        'ano': ano,
        'docente_selecionado': docente_selecionado,
        'alunos_count': alunos_count,
        'situacao_all': situacao_all,
        'situacao_selecionada': situacao_selecionada
    }

    return render(request, 'relatorioslist.html', contexto)