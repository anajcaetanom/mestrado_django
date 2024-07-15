from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .models import Aluno
from .forms import AlunoForm, AlunoForm_Edit
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from turmas.models import Turma
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse

def pesquisa_aluno(request):
    query = request.GET.get('aluno')

    if query:
        # Dividindo a consulta em palavras-chave
        keywords = query.split()
        
        # Criando uma lista de Q objects para pesquisa flexível
        query_list = []
        for keyword in keywords:
            query_list.append(Q(nome__icontains=keyword) | Q(sobrenome__icontains=keyword))
        
        # Combinando os Q objects usando operador OR
        pesquisa = Q()
        for query_item in query_list:
            pesquisa |= query_item
        
        # Realizando a consulta no banco de dados
        alunosValues = Aluno.objects.filter(pesquisa)

    else:
        alunosValues = Aluno.objects.all().order_by('nome')

    return alunosValues

def alunos(request):
    alunosValues = pesquisa_aluno(request)
    defendeu = request.GET.get('defendeu')
    turmas_selecionadas = request.GET.getlist('turma')

    if defendeu == '0':
        alunosValues = alunosValues.filter(defesa=True)
    elif defendeu == '1':
        alunosValues = alunosValues.filter(defesa=False)

    aluno_defendeu = Aluno.objects.filter(defesa=True) # Pode ser retirado junto com a parte do html
    contador = Aluno.objects.filter(defesa=True).count() # Pode ser retirado junto com a parte do html

    todas_turmas = Turma.objects.all().order_by('nome')

    turmas_query = Q()
    for curso_id in turmas_selecionadas:
        turmas_query |= Q(turma_id=curso_id)

    alunosValues = alunosValues.filter(turmas_query)

    alunosAtivos = alunosValues.filter(situacao= 'E')

    alunosDesistentes = alunosValues.filter(situacao='D')

    alunosJubilados = alunosValues.filter(situacao= 'J')

    alunosTrancados = alunosValues.filter(situacao= 'T')

    alunosConcluidos = alunosValues.filter(situacao= 'C')

    context = {
        'alunosValues': alunosValues, 
        'aluno_defendeu': aluno_defendeu, # Pode ser retirado junto com a parte do html
        'contador': contador, # Pode ser retirado junto com a parte do html
        'turmas': todas_turmas, 
        'turmas_selecionadas': turmas_selecionadas,
        'alunosAtivos' : alunosAtivos,
        'alunosDesistentes' : alunosDesistentes,
        'alunosJubilados' : alunosJubilados,
        'alunosTrancados' : alunosTrancados,
        'alunosConcluidos' : alunosConcluidos,
        }
    
    return render(request, 'alunosList.html', context)


def alunoInfo(request, prefix, id):
    alunoID = get_object_or_404(Aluno, id=id)
    context = {'alunoID': alunoID, 'prefix': prefix}
    return render(request, 'alunoInfo.html', context)

@login_required
def criar_aluno(request):
    form = AlunoForm()
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos')

    return render(request, 'criar_aluno.html', {'form': form})

@login_required
def editar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        form = AlunoForm_Edit(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            prefixed_url = reverse('alunoInfo', kwargs={'prefix': 'alunos', 'id': aluno.id})
            return redirect(prefixed_url)
        else:
            messages.error(request, "O formulário contém erros. Por favor, corrija-os.")
            # Re-renderize o formulário com os erros
            return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})
    else:
        form = AlunoForm_Edit(instance=aluno)
        return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno}) 
     

@login_required 
def excluir_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos')

    return render(request, {'aluno': aluno})