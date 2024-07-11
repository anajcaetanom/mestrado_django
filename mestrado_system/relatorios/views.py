from django.shortcuts import render
from alunos.models import Aluno
from turmas.models import Turma
from docentes.models import Docente
from django.contrib import messages
from datetime import datetime


# Create your views here.

def relatorioslist(request):
    alunos = Aluno.objects.all()
    todas_as_turmas = Turma.objects.all().values().order_by('nome')
    todos_os_docentes = Docente.objects.all().values().order_by('nome')

    turmas_selecionadas_ids = request.GET.getlist('turmas')

    if turmas_selecionadas_ids:
        alunos = alunos.filter(turma__id__in=turmas_selecionadas_ids)

    return render(request, "relatorioslist.html", {'todas_as_turmas': todas_as_turmas, 'todos_os_docentes': todos_os_docentes})

def filtrar_alunos(request):
    turma_selecionada = request.GET.get('turma')
    docente_selecionado = request.GET.get('docente')
    situacao_selecionada = request.GET.get('situacao_all')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    alunos = Aluno.objects.all().order_by('situacao')
    turmas = Turma.objects.all()
    docentes = Docente.objects.all()
    situacao_all = Aluno.SITUACAO_CHOICES

    if turma_selecionada:
        alunos = alunos.filter(turma__id=turma_selecionada)

    if docente_selecionado:
        alunos = alunos.filter(orientadores__id=docente_selecionado)

    if situacao_selecionada:
        alunos = alunos.filter(situacao=situacao_selecionada)
    
    if data_inicio:
        try:
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
            alunos = alunos.filter(data_defesa__gte=data_inicio)
        except ValueError:
            messages.error(request, 'Por favor, insira uma data de início válida no formato AAAA-MM-DD.')

    if data_fim:
        try:
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
            alunos = alunos.filter(data_defesa__lte=data_fim)
        except ValueError:
            messages.error(request, 'Por favor, insira uma data final válida no formato AAAA-MM-DD.')

    alunos_count = alunos.count()

    contexto = {
        'alunos': alunos,
        'turmas': turmas,
        'docentes': docentes,
        'turma_selecionada': turma_selecionada,
        'docente_selecionado': docente_selecionado,
        'alunos_count': alunos_count,
        'situacao_all': situacao_all,
        'situacao_selecionada': situacao_selecionada,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }

    return render(request, 'relatorioslist.html', contexto)