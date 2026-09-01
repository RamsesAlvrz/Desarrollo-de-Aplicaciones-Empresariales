from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'medico', 'especialidad', 'fecha_hora', 'estado']
        widgets = {
            'paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan Pérez'}),
            'medico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Dr. Ramses Alvarez'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Traumatología'}),
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }