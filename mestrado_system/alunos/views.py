from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Aluno
from .forms import AlunoForm

def alunos(request):
  alunosValues = Aluno.objects.all().values()
  template = loader.get_template('alunosList.html')
  context = {'alunosValues': alunosValues, }
  return HttpResponse(template.render(context, request))

def alunoInfo(request, id):
  alunoID = Aluno.objects.get(id=id)
  template = loader.get_template('alunoInfo.html')
  context = {'alunoID': alunoID, }
  return HttpResponse(template.render(context, request))

def criar_aluno(request):
    form = AlunoForm()
    
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos')

    return render(request, 'criar_aluno.html', {'form': form})
