from django.urls import path
from .views import index
app_name = 'Bauman_Consulting'

urlpatterns = [
    path('',index, name='index')
]
