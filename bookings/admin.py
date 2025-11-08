from django.contrib import admin
from .models import Service, Client, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("client", "service", "start_datetime")
    list_filter = ("service",)
    search_fields = ("client__name", "client__phone")

