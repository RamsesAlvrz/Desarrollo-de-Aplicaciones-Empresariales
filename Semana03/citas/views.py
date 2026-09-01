from django.shortcuts import render, redirect
from .models import Cita
from .forms import CitaForm

def cita_list_view(request):
    citas = Cita.objects.all().order_by('-id')  # ORM: Consulta la base de datos SQLite
    return render(request, 'citas/cita_list.html', {'citas': citas})

def cita_create_view(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()  # ORM: Guarda el registro persistente en SQLite
            return redirect('citas:list')
    else:
        form = CitaForm()
    return render(request, 'citas/cita_form.html', {'form': form})