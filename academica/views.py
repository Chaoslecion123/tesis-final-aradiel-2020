from django.shortcuts import render

# formularios
from .forms import *

# Modelos 
from .models import *

def nivel_list(request):
    niveles = Nivel.objects.all()
    ctx = {'niveles':niveles}
    return render(request,'academica/nivel_list.html',ctx)

def nivel_create(request):
    form = NivelForm()
    if request.method == 'POST':
        form = NivelForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'form':form
    }
    return render(request,'academica/nivel_create.html',ctx)


def matricula_create(request):
    form = MatriculaForm()
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
    ctx = {
        'form':form
    }
    return render(request,'academica/matricula_create.html',ctx)
    