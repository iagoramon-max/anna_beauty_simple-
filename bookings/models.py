from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField(default=60)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service.name} - {self.client.name} - {self.start_datetime.strftime('%d/%m/%Y %H:%M')}"

