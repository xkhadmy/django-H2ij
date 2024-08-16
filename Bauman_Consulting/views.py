from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import FileResponse
import os
from django.conf import settings  # добавьте этот импорт
from .forms import ContactFormForm, KaufenFormForm
from django.core.mail import send_mail
from .models import ContactForm

 

 
import io
 
from django.db.models import Count
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'Home.html' )

def page_Unterstutzung(request):
    return render(request, "utils/buttons/Unterstutzung.html")


def page_Referenzen(request):
    return render(request, "utils/buttons/Referenzen.html")


def page_Literatur(request):
    return render(request, "utils/buttons/Literatur.html")


def page_Kontakt(request):
    return render(request, "utils/buttons/Kontakt.html")


def page_Unser_Angebot(request):
    return render(request, "utils/buttons/Unser_Angebot.html")


def page_Bestellen(request):
    return render(request, "utils/buttons/Bestellen.html")


def page_Organisatorisches_Sicherheitskonzept(request):
    return render(request, "utils/buttons/Organisatorisches_Sicherheitskonzept.html")


def page_Technisches_Sicherheitskonzept(request):
    return render(request, "utils/buttons/Technisches_Sicherheitskonzept.html")

def contact_form_view(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # form.save()  # Закомментируйте эту строку, чтобы не сохранять данные в базу

            # Отправка email peter.baumann.sulz@bluewin.ch
            subject = "New contact form submission"
            message = f"""
            Thema: {form.cleaned_data['thema']}
            Vorname: {form.cleaned_data['vorname']}
            Nachname: {form.cleaned_data['nachname']}
            Firma: {form.cleaned_data['firma']}
            Telephone: {form.cleaned_data['telephone']}
            E-mail: {form.cleaned_data['email']}
            Betreff: {form.cleaned_data['betreff']}
            Nachricht: {form.cleaned_data['nachricht']}
            """
            recipient_list = ["dimaadboos@gmail.com"]

            send_mail(subject, message, "sender@example.com", recipient_list)

            return redirect("index")
    else:
        form = ContactFormForm()
    return render(request, "contact_form.html", {"form": form})
