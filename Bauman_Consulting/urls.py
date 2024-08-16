from django.urls import path
from .views import index
from .views import (
    page_Unser_Angebot,
    page_Kontakt,
    page_Organisatorisches_Sicherheitskonzept,
    page_Technisches_Sicherheitskonzept,
    page_Literatur,
    page_Bestellen,
    contact_form_view,
)

app_name = 'Bauman_Consulting'

urlpatterns = [
    path('',index, name='index'),
    path("Unser_Angebot/", page_Unser_Angebot, name="Unser_Angebot"),
    path("Literatur/", page_Literatur, name="Literatur"),
    path("Kontakt/", page_Kontakt, name="Kontakt"),
    path("Bestellen/", page_Bestellen, name="Bestellen"),
    path("contact_form/", contact_form_view, name="contact_form "),
    path("Organisatorisches_Sicherheitskonzept/",
        page_Organisatorisches_Sicherheitskonzept,
        name="Organisatorisches_Sicherheitskonzept",
    ),
    path(
        "Technisches_Sicherheitskonzept/",
        page_Technisches_Sicherheitskonzept,
        name="Technisches_Sicherheitskonzept",
    ),
    
    
]
