from django.urls import path
from .views import index
from .views import (

    page_Kontakt,
    
)

app_name = 'Bauman_Consulting'

urlpatterns = [
    path('',index, name='index'),
    
    path("Kontakt/", page_Kontakt, name="Kontakt"),
    
]
