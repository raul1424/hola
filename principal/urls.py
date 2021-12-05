from django.urls import path
from . import views

urlpatterns = [
    path("",views.holaDjango, name="holaDjango"),
    path("pepe",views.pepe, name="Hola pepe!"),
    path('<str:nombre>', views.holaTu, name='Hola Tu!')
]