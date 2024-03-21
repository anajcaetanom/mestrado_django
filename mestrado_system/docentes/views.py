from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Docente
from .forms import DocenteForm
from django.db.models import Q

def docentes(request):
    query = request.GET.get('q')
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
        docentesValues = Docente.objects.filter(pesquisa)
    else:
        docentesValues = Docente.objects.all()
    
    context = {'docentesValues': docentesValues}
    return render(request, 'docentesList.html', context)






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