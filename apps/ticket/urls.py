from django.urls import path
from .views import ticket

app_name = "ticket_app"

urlpatterns = [
    path('', ticket, name="ticket"),
]

