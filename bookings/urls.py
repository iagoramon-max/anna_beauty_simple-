from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book_view, name="book"),
    path("confirmation/", views.confirmation_view, name="confirmation"),
    path("my-appointments/", views.my_appointments_view, name="my_appointments"),
]
