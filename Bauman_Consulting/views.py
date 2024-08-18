from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import FileResponse
import os
from django.conf import settings  # добавьте этот импорт
from .forms import ContactFormForm, KaufenFormForm
from django.core.mail import send_mail
 
 
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

def kaufen_form_view(request):
    if request.method == "POST":
        form = KaufenFormForm(request.POST)
        if form.is_valid():
            #form.save()
            # Отправка email
            subject = "New contact form submission"
            message = f"""
            ---------------Rechnungsadresse---------------
            Vorname: {form.cleaned_data['vorname']}
            Nachname: {form.cleaned_data['nachname']}
            Firma: {form.cleaned_data['firma']}
            Telephone: {form.cleaned_data['telephone']}
            E-mail: {form.cleaned_data['email']}
            Betreff: {form.cleaned_data['betreff']}
            Strasse: {form.cleaned_data['strasse']}
            Hausnummer: {form.cleaned_data['hausnummer']} 
            PLZ: {form.cleaned_data['plz']}
            Ort: {form.cleaned_data['ort']} 
            Nachricht: {form.cleaned_data['nachricht']}
            ---------------Lieferadresse------------------
            Vorname: {form.cleaned_data['vorname_l']}
            Nachname: {form.cleaned_data['nachname_l']}
            Firma: {form.cleaned_data['firma_l']}
            Telephone: {form.cleaned_data['telephone_l']}
            E-mail: {form.cleaned_data['email_l']}
            Betreff: {form.cleaned_data['betreff_l']}
            Strasse: {form.cleaned_data['strasse_l']}
            Hausnummer: {form.cleaned_data['hausnummer_l']} 
            PLZ: {form.cleaned_data['plz_l']}
            Ort: {form.cleaned_data['ort_l']}
            Nachricht: {form.cleaned_data['nachricht_l']}
            """
            recipient_list = ["dimaadboos@gmail.com"]  # Замените на ваш email адрес

            send_mail(subject, message, "sender@example.com", recipient_list)

            print("Форма сохранена успешно")
            return redirect("index")
        else:
            print("Форма недействительна", form.errors)
    else:
        form = KaufenFormForm()
    return render(request, "utils/buttons/Bestellen.html", {"form": form})