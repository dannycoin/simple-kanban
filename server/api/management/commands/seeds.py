from django.core.management.base import BaseCommand
from api.models import Task

class Command(BaseCommand):
    help = 'Agrega datos de prueba a la base de datos'

    def handle(self, *args, **kwargs):
        initial_tasks = [
            {
                'name': 'Realizar investigación de mercado',
                'description': 'Investigar el mercado para identificar oportunidades',
                'assignee': 'Equipo de marketing',
                'status': 'pendiente'
            },
            {
                'name': 'Desarrollar estrategia de negocios',
                'description': 'Crear un plan estratégico para el negocio',
                'assignee': 'Equipo directivo',
                'status': 'procesando'
            },
            {
                'name': 'Implementar plan de marketing',
                'description': 'Ejecutar el plan de marketing para promocionar el negocio',
                'assignee': 'Equipo de marketing',
                'status': 'finalizado'
            },
        ]

        for task_data in initial_tasks:
            task = Task(**task_data)
            task.save()