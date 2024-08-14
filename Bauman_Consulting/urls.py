from django.urls import path
from .views import index
from .views import (
    page_Unser_Angebot,
    page_Kontakt,
    page_Organisatorisches_Sicherheitskonzept,
    page_Technisches_Sicherheitskonzept
)

app_name = 'Bauman_Consulting'

urlpatterns = [
    path('',index, name='index'),
    path("Unser_Angebot/", page_Unser_Angebot, name="Unser_Angebot"),
    path("Kontakt/", page_Kontakt, name="Kontakt"),
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
