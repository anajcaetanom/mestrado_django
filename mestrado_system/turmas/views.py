from django.http import HttpResponse
from django.template import loader
from .models import Turma
from django.shortcuts import render, get_object_or_404
from .forms import TurmaForm
from django.shortcuts import redirect
from alunos.models import Aluno
from alunos.views import *
from django.contrib.auth.decorators import login_required
from users.urls import *

def turmas(request):
    all_turmas = Turma.objects.all().values()
    template = loader.get_template('display_turmas.html')
    context = {'all_turmas': all_turmas,}
    return HttpResponse(template.render(context, request))

def details(request, id):
    myturma = Turma.objects.get(id=id)
    aluno_turma = Aluno.objects.filter(curso=myturma)
    context = {'myturma': myturma, 'aluno_turma' : aluno_turma}
    return render(request, "details.html", context)

def main(request):
    return render(request, "main.html")

@login_required
def editar_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('details', id=turma_id)
    else:
        form = TurmaForm(instance=turma)

    return render(request, 'editar_turma.html', {'form': form, 'turma': turma})

@login_required
def criar_turma(request):

    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turmas')
    else:
        form = TurmaForm()

    return render(request, 'criar_turma.html', {'form': form})

@login_required
def excluir_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    
    if request.method == 'POST':
        turma.delete()
        return redirect('turmas')

    return render(request, {'turma': turma})

