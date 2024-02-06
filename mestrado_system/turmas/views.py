from django.http import HttpResponse
from django.template import loader
from .models import Turma

def turmas(request):
  all_turmas = Turma.objects.all().values()
  template = loader.get_template('display_turmas.html')
  context = {'all_turmas': all_turmas, }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myturma = Turma.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {'myturma': myturma, }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())