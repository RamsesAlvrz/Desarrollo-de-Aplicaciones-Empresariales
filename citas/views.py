from django.shortcuts import render, redirect
from .models import get_all_citas, add_cita
from .forms import CitaForm

def cita_list_view(request):
    """Muestra el listado completo de citas médicas."""
    citas = get_all_citas()
    return render(request, 'citas/cita_list.html', {'citas': citas})

def cita_create_view(request):
    """Procesa el formulario y agrega una nueva cita a la lista en memoria."""
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            # Extraer datos validados
            paciente = form.cleaned_data['paciente']
            medico = form.cleaned_data['medico']
            especialidad = form.cleaned_data['especialidad']
            fecha_hora = form.cleaned_data['fecha_hora']
            estado = form.cleaned_data['estado']
            
            # Guardar en memoria RAM (CITAS_DB)
            add_cita(paciente, medico, especialidad, fecha_hora, estado)
            
            # Redirigir al listado de citas
            return redirect('citas:list')
    else:
        form = CitaForm()

    return render(request, 'citas/cita_form.html', {'form': form})