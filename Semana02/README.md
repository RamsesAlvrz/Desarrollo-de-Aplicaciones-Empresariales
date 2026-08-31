# Módulo de Gestión de Citas Médicas (`citas`)

## Problemática
En la recepción de una clínica médica, el registro manual genera duplicidad de horarios y retrasos. Esta solución digital centralizada permite consultar disponibilidad y registrar citas en tiempo real.

## Requisitos Funcionales
- **RF1:** Visualizar el listado general de citas médicas.
- **RF2:** Proveer un formulario para registrar nuevas citas.
- **RF3:** Validar campos obligatorios (paciente, médico, especialidad, fecha/hora y estado).
- **RF4:** Almacenar temporalmente los datos en memoria RAM (`models.py`).
- **RF5:** Redirigir al listado tras registrar exitosamente una cita.

## Estructura de la App
- **App creada:** `citas` (integrada junto a `core` en `INSTALLED_APPS`).
- **Model:** Manejo de datos estáticos en memoria RAM (`CITAS_DB`).
- **Form:** Implementación de `CitaForm` con validación y formateo de datos.