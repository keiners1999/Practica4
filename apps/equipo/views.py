from django.shortcuts import render, redirect
from apps.equipo.Formmantenimiento import MantenimientoForm
from apps.equipo.models import Mantenimiento

# Create your views here.

def inicio(request):    
    mantenimiento = Mantenimiento.objects.all().order_by('id')
    return render(request,'paginas/mantenimiento.html', {'mantenimiento': mantenimiento})

def create(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = MantenimientoForm()
        return render(request,'paginas/mantenimientoForm.html', {'form': form})
    
    
def update(request,id):
    mantenimiento = Mantenimiento.objects.get(id=id)
    if request.method == 'GET':
        form = MantenimientoForm(instance=mantenimiento)
    else:
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    return render(request, 'paginas/mantenimientoForm.html', {'form': form})

def delete(request, id):
    mantenimiento = Mantenimiento.objects.get(id=id)
    mantenimiento.delete()
    return redirect('inicio')