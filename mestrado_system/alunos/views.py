from django.http import HttpResponse
from django.template import loader
from .models import Aluno

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

