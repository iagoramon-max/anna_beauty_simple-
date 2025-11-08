from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Appointment, Client, Service
import datetime, requests, os

class AppointmentForm(forms.Form):
    client_name = forms.CharField(max_length=120, label="Seu nome")
    client_phone = forms.CharField(max_length=20, label="WhatsApp")
    client_email = forms.EmailField(required=False, label="E-mail")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="Serviço")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    notes = forms.CharField(widget=forms.Textarea, required=False)
    recaptcha_token = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        cleaned = super().clean()
        date = cleaned.get("date")
        time = cleaned.get("time")
        service = cleaned.get("service")
        token = cleaned.get("recaptcha_token")

        # reCAPTCHA
        if not token:
            raise ValidationError("🧠 Esqueceu do teste de segurança, gata.")
        secret = os.getenv("RECAPTCHA_SECRET_KEY")
        try:
            res = requests.post("https://www.google.com/recaptcha/api/siteverify",
                                data={"secret": secret, "response": token})
            if not res.json().get("success"):
                raise ValidationError("🤖 Hmm... parece que você é um robô, flor?")
        except Exception:
            raise ValidationError("😅 Probleminha na verificação, tenta de novo, linda.")

        start_dt = timezone.make_aware(datetime.datetime.combine(date, time))
        weekday = start_dt.weekday()

        if weekday > 5:
            raise ValidationError("💤 Domingo é dia de descanso, amor. Escolhe outro dia!")

        allowed = (datetime.time(8, 0), datetime.time(18, 0)) if weekday < 5 else (datetime.time(8, 0), datetime.time(12, 0))
        if not (allowed[0] <= time <= allowed[1]):
            raise ValidationError("⏰ Horário fora do expediente, linda!")

        duration = datetime.timedelta(minutes=service.duration_minutes)
        end_dt = start_dt + duration

        from django.db import transaction
        with transaction.atomic():
            conflict = Appointment.objects.select_for_update().filter(
                start_datetime__lt=end_dt,
                start_datetime__gte=start_dt - duration
            ).exists()
            if conflict:
                raise ValidationError("🚫 Já tem uma cliente marcada nesse horário, miga!")

        cleaned["start_datetime"] = start_dt
        return cleaned

