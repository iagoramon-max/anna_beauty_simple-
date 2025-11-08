from django.urls import path
from . import views

app_name = "bookings"

urlpatterns = [
    path("", views.home, name="home"),
    path("book/", views.book_view, name="book"),
    path("confirmation/", views.confirmation, name="confirmation"),
    path("minhas-reservas/", views.my_appointments, name="my_appointments"),
]

