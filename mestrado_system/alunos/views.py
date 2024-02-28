from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .models import Aluno
from .forms import AlunoForm
from django.contrib.auth.decorators import login_required

def alunos(request):
    alunosValues = Aluno.objects.all().values()
    template = loader.get_template('alunosList.html')
    context = {'alunosValues': alunosValues, }
    return HttpResponse(template.render(context, request))

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
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunoInfo', id=aluno.id)
    else:
        form = AlunoForm(instance=aluno)
        return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})

@login_required 
def excluir_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos')

    return render(request, {'aluno': aluno})
