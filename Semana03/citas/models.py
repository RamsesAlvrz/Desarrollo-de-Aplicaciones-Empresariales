from django.db import models

class Cita(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
    ]

    paciente = models.CharField(max_length=100, verbose_name="Paciente")
    medico = models.CharField(max_length=100, verbose_name="Médico")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    fecha_hora = models.DateTimeField(verbose_name="Fecha y Hora")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente', verbose_name="Estado")

    def __str__(self):
        return f"{self.paciente} - {self.medico} ({self.fecha_hora})"