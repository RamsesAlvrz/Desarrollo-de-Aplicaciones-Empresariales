from django import forms

ESTADO_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('Confirmada', 'Confirmada'),
    ('Cancelada', 'Cancelada'),
]

class CitaForm(forms.Form):
    paciente = forms.CharField(
        label="Nombre del Paciente",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Juan Pérez'
        })
    )
    medico = forms.CharField(
        label="Médico Tratante",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Ramses Alvarez'
        })
    )
    especialidad = forms.CharField(
        label="Especialidad Médica",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Traumatología'
        })
    )
    fecha_hora = forms.CharField(
        label="Fecha y Hora",
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'  # <--- Activa el calendario y reloj interactivo
        })
    )
    estado = forms.ChoiceField(
        label="Estado de la Cita",
        choices=ESTADO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    def clean_medico(self):
        medico = self.cleaned_data.get('medico', '').strip()
        if not (medico.startswith('Dr.') or medico.startswith('Dra.')):
            medico = f"Dr. {medico}"
        return medico

    # Formatear la fecha para sustituir la 'T' del selector por un espacio
    def clean_fecha_hora(self):
        fecha = self.cleaned_data.get('fecha_hora', '')
        return fecha.replace('T', ' ')