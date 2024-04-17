from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .models import Aluno
from .forms import AlunoForm, FiltroDataForm, AlunoForm_Edit, AlunoForm_Situacao
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from turmas.models import Turma
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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
        alunosValues = Aluno.objects.all()

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

    todas_turmas = Turma.objects.all()

    turmas_query = Q()
    for turma_id in turmas_selecionadas:
        turmas_query |= Q(curso_id=turma_id)
    alunosValues = alunosValues.filter(turmas_query)

    context = {
        'alunosValues': alunosValues, 
        'aluno_defendeu': aluno_defendeu, # Pode ser retirado junto com a parte do html
        'contador': contador, # Pode ser retirado junto com a parte do html
        'turmas': todas_turmas, 
        'turmas_selecionadas': turmas_selecionadas,
        }
    
    return render(request, 'alunosList.html', context)


def alunos_desistencia(request):
    alunosValues = pesquisa_aluno(request)

    alunosValues = Aluno.objects.filter(situacao = 'D')

    context = {
        'alunosValues': alunosValues, 
        }
    
    return render(request, 'alunoList_desistencia.html', context)


def alunoInfo(request, id):
    alunoID = get_object_or_404(Aluno, id=id)
    template = loader.get_template('alunoInfo.html')
    context = {'alunoID': alunoID, }
    return HttpResponse(template.render(context, request))

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
            return redirect('alunoInfo', id=aluno.id)
        else:
            messages.error(request, "O formulário contém erros. Por favor, corrija-os.")
            # Re-renderize o formulário com os erros
            return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})
    else:
        form = AlunoForm_Edit(instance=aluno)
        return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno}) 
    
def desistencia(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        form = AlunoForm_Situacao(request.POST, instance=aluno)
        if form.is_valid():
            alunoSituacao = form.save(commit=False)
            alunoSituacao.situacao = "D"
            alunoSituacao.save()
            return redirect('alunoInfo', id=aluno.id)
        else:
            messages.error(request, "O formulário contém erros. Por favor, corrija-os.")
            # Re-renderize o formulário com os erros
            return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})
    else:
        form = AlunoForm_Situacao(instance=aluno)
        return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})

def jubilado(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        form = AlunoForm_Situacao(request.POST, instance=aluno)
        if form.is_valid():
            alunoSituacao = form.save(commit=False)
            alunoSituacao.situacao = "J"
            alunoSituacao.save()
            return redirect('alunoInfo', id=aluno.id)
        else:
            messages.error(request, "O formulário contém erros. Por favor, corrija-os.")
            # Re-renderize o formulário com os erros
            return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})
    else:
        form = AlunoForm_Situacao(instance=aluno)
        return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})

def trancamento(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        form = AlunoForm_Situacao(request.POST, instance=aluno)
        if form.is_valid():
            alunoSituacao = form.save(commit=False)
            alunoSituacao.situacao = "T"
            alunoSituacao.save()
            return redirect('alunoInfo', id=aluno.id)
        else:
            messages.error(request, "O formulário contém erros. Por favor, corrija-os.")
            # Re-renderize o formulário com os erros
            return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})
    else:
        form = AlunoForm_Situacao(instance=aluno)
        return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})
     

@login_required 
def excluir_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos')

    return render(request, {'aluno': aluno})

def filtrar_alunos(request):
    if request.method == 'GET':
        form = FiltroDataForm(request.GET)
        if form.is_valid():
            data_inicio = form.cleaned_data.get('data_inicio')
            data_fim = form.cleaned_data.get('data_fim')
            
            # Filtre os alunos com base nas datas fornecidas
            alunos = Aluno.objects.all()
            if data_inicio:
                alunos = alunos.filter(data_defesa__gte=data_inicio)
            if data_fim:
                alunos = alunos.filter(data_defesa__lte=data_fim)
            
            return render(request, 'teste.html', {'alunos': alunos, 'form': form})
    else:
        form = FiltroDataForm()

    return render(request, 'teste.html', {'form': form})