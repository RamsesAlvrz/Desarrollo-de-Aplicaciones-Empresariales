# citas/models.py

# Lista como nuestra base de datos estática
CITAS_DB = [
    {
        "id": 1,
        "paciente": "Carlos Mendoza",
        "medico": "Dr. Roberto Gómez",
        "especialidad": "Cardiología",
        "fecha_hora": "2026-09-01 09:00",
        "estado": "Confirmada"
    },
    {
        "id": 2,
        "paciente": "Ana Lucía Torres",
        "medico": "Dra. María Paredes",
        "especialidad": "Pediatría",
        "fecha_hora": "2026-09-01 10:30",
        "estado": "Pendiente"
    },
    {
        "id": 3,
        "paciente": "Jorge Luis Ramos",
        "medico": "Dr. Fernando Ruiz",
        "especialidad": "Dermatología",
        "fecha_hora": "2026-09-01 11:15",
        "estado": "Confirmada"
    },
    {
        "id": 4,
        "paciente": "Elena Rostova",
        "medico": "Dra. Sofía Vargas",
        "especialidad": "Ginecología",
        "fecha_hora": "2026-09-02 08:30",
        "estado": "Pendiente"
    },
    {
        "id": 5,
        "paciente": "Mateo Delgado",
        "medico": "Dr. Roberto Gómez",
        "especialidad": "Cardiología",
        "fecha_hora": "2026-09-02 14:00",
        "estado": "Confirmada"
    },
]

def get_all_citas():
    """Retorna la lista completa de citas médicas registradas en memoria."""
    return CITAS_DB

def add_cita(paciente, medico, especialidad, fecha_hora, estado):
    """Agrega una nueva cita médica a la estructura en memoria asignando un ID autoincremental."""
    nuevo_id = len(CITAS_DB) + 1 if CITAS_DB else 1
    nueva_cita = {
        "id": nuevo_id,
        "paciente": paciente,
        "medico": medico,
        "especialidad": especialidad,
        "fecha_hora": fecha_hora,
        "estado": estado
    }
    CITAS_DB.append(nueva_cita)
    return nueva_cita