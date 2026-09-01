from django.urls import path
from .views import cita_list_view, cita_create_view

app_name = 'citas'

urlpatterns = [
    path('', cita_list_view, name='list'),
    path('crear/', cita_create_view, name='create'),
]