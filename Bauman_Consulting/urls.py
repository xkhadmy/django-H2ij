from django.urls import path
from .views import index
from .views import (
    page_Unser_Angebot,
    page_Kontakt,
    
)

app_name = 'Bauman_Consulting'

urlpatterns = [
    path('',index, name='index'),
    path("Unser_Angebot/", page_Unser_Angebot, name="Unser_Angebot"),
    path("Kontakt/", page_Kontakt, name="Kontakt"),
    
    
]
