# Laboratorio 3: Persistencia de Datos con Django ORM y SQLite (Parte 1)

**Curso:** Desarrollo de Aplicaciones Empresariales  
**Institución:** Tecsup  
**Semana:** 03  
**Alumno:** Ramses Alvarez  

---

## 📌 Descripción del Proyecto

En esta primera parte del laboratorio se realizó la migración del módulo de gestión de citas médicas (`citas`), evolucionando desde una estructura de almacenamiento temporal en memoria RAM hacia un sistema de persistencia completo utilizando el **ORM de Django** y **SQLite** como motor de base de datos relacional.

Con esta implementación, todos los registros de pacientes y citas médicas creados desde la interfaz web se almacenan permanentemente en el disco dentro de la base de datos `db.sqlite3`.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.12+
* **Framework Web:** Django 6.1+
* **Base de Datos:** SQLite 3
* **Control de Versiones:** Git & GitHub
* **Entorno Virtual:** `venv`

---

## 🚀 Cambios e Implementaciones Realizadas

### 1. Definición del Modelo de Datos (`models.py`)
Se reemplazó el almacenamiento en memoria por el modelo `Cita`, mapeando las propiedades necesarias al esquema relacional:
* `paciente`: `CharField`
* `medico`: `CharField`
* `especialidad`: `CharField`
* `fecha`: `DateField`
* `hora`: `TimeField`
* `estado`: `CharField` (con opciones de selección `Pendiente`, `Confirmada`, `Cancelada`)

### 2. Gestión de Migraciones
Se generaron y aplicaron las migraciones del modelo hacia la base de datos SQLite mediante los comandos:
```bash
python manage.py makemigrations citas
python manage.py migrate
python manage.py showmigrations citas
