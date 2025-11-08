from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from .forms import AppointmentForm
from .models import Client, Appointment
from .tasks import send_whatsapp_confirmation_task

def home(request):
    return render(request, "home.html")

def book_view(request):
    from django.conf import settings
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            client, _ = Client.objects.get_or_create(
                phone=cd["client_phone"],
                defaults={"name": cd["client_name"], "email": cd.get("client_email")}
            )
            appointment = Appointment.objects.create(
                service=cd["service"],
                client=client,
                start_datetime=cd["start_datetime"],
                notes=cd["notes"]
            )
            send_whatsapp_confirmation_task.delay(appointment.id)
            return redirect(reverse("bookings:confirmation") + f"?id={appointment.id}")
        else:
            messages.error(request, "💅 Ops! Corrige os errinhos e tenta de novo, princesa.")
    else:
        form = AppointmentForm()

    return render(request, "book.html", {"form": form, "RECAPTCHA_SITE_KEY": getattr(settings, "RECAPTCHA_SITE_KEY", "")})

def confirmation(request):
    appt_id = request.GET.get("id")
    appt = Appointment.objects.get(id=appt_id)
    return render(request, "confirmation.html", {"appointment": appt})

def my_appointments(request):
    phone = request.GET.get("phone")
    if not phone:
        messages.error(request, "✉️ Esqueceu do WhatsApp, gata!")
        return render(request, "my_appointments.html")

    client = Client.objects.filter(phone__icontains=phone).first()
    if not client:
        messages.error(request, "💔 Nenhum agendamento com esse número, flor.")
        return render(request, "my_appointments.html")

    appointments = Appointment.objects.filter(client=client).order_by("start_datetime")
    now = timezone.localtime(timezone.now())
    for a in appointments:
        a.days_left = (a.start_datetime - now).days
    return render(request, "my_appointments.html", {"client": client, "appointments": appointments})

