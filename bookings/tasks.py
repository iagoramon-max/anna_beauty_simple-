from celery import shared_task
from .models import Appointment
from .utils import send_whatsapp_confirmation

@shared_task
def send_whatsapp_confirmation_task(appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        send_whatsapp_confirmation(appointment)
    except Appointment.DoesNotExist:
        print("💔 Agendamento não encontrado, gatinha.")

