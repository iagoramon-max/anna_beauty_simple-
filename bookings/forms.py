from django import forms
from .models import Client, Appointment, Service
from django.utils import timezone

class AppointmentForm(forms.Form):
    name = forms.CharField(label="Seu nome", max_length=100)
    phone = forms.CharField(label="WhatsApp", max_length=20)
    email = forms.EmailField(label="E-mail", required=False)
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="Serviço")
    date = forms.DateField(label="Data", widget=forms.DateInput(attrs={"type": "date"}))
    time = forms.TimeField(label="Hora", widget=forms.TimeInput(attrs={"type": "time"}))
    notes = forms.CharField(label="Observações", widget=forms.Textarea, required=False)

    def save(self):
        client, _ = Client.objects.get_or_create(
            name=self.cleaned_data["name"],
            phone=self.cleaned_data["phone"],
            email=self.cleaned_data["email"],
        )

        date = self.cleaned_data["date"]
        time = self.cleaned_data["time"]
        start_datetime = timezone.make_aware(
            timezone.datetime.combine(date, time),
            timezone.get_current_timezone()
        )

        appointment = Appointment.objects.create(
            client=client,
            service=self.cleaned_data["service"],
            start_datetime=start_datetime,
            notes=self.cleaned_data["notes"]
        )
        return appointment
