from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Docente
from .forms import DocenteForm

def docentes(request):
    docentesValues = Docente.objects.all().values()
    template = loader.get_template('docentesList.html')
    context = {'docentesValues': docentesValues, }
    return HttpResponse(template.render(context, request))

def docenteInfo(request, id):
    docenteID = get_object_or_404(Docente, id=id)
    template = loader.get_template('docenteInfo.html')
    alunos_orientados = docenteID.alunos_orientados.all()
    context = {'docenteID': docenteID, 'alunos_orientados': alunos_orientados }
    return HttpResponse(template.render(context, request))

@login_required
def criar_docente(request):
    form = DocenteForm()
    
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docentes')

    return render(request, 'criar_docente.html', {'form': form})

@login_required
def editar_docente(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('docenteInfo', id=docente.id)
    else:
        form = DocenteForm(instance=docente)
        return render(request, 'editar_docente.html', {'form': form, 'docente': docente})

@login_required 
def excluir_docente(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    
    if request.method == 'POST':
        docente.delete()
        return redirect('docente')

    return render(request, {'docente': docente})