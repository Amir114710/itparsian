from django.shortcuts import render, redirect
from .models import Ticket
import time


def ticket(request):
    success = True
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('msg')
        Ticket.objects.create(email=email, phone=phone, message=message)
        time.sleep(1)
        return redirect(request.META['HTTP_REFERER'])

