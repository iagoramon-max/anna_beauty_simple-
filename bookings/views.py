from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import AppointmentForm
from .models import Appointment

def book_view(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("confirmation")
    else:
        form = AppointmentForm()
    return render(request, "book.html", {"form": form})

def confirmation_view(request):
    return render(request, "confirmation.html")

def my_appointments_view(request):
    now = timezone.now()
    appointments = Appointment.objects.all().order_by("start_datetime")
    return render(request, "my_appointments.html", {"appointments": appointments, "now": now})
