import urllib.parse
from django.utils import timezone
from django.conf import settings

def send_whatsapp_confirmation(appointment):
    now = timezone.localtime(timezone.now())
    msg = (
        f"Oi, {appointment.client.name.split()[0]}! 💖\n"
        f"Seu agendamento no *Anna Beauty Studio* foi recebido com sucesso!\n\n"
        f"📅 {appointment.start_datetime.strftime('%d/%m/%Y %H:%M')} — {appointment.service.name}\n"
        f"✨ Faltam {(appointment.start_datetime - now).days} dias pro seu momento de beleza!\n\n"
        f"Beijos 😘"
    )

    phone_clean = appointment.client.phone.replace("+", "")
    link = f"https://wa.me/{phone_clean}?text={urllib.parse.quote(msg)}"
    print(f"💬 Link de confirmação: {link}")

    # opcionalmente envia link via print/log ou e-mail para admin
    return link

