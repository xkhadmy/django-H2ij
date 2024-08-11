from django.shortcuts import render

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