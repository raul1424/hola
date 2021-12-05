from django.urls import path
from . import views

urlpatterns = [
    path("",views.holaDjango, name="holaDjango"),
    path("pepe",views.pepe, name="Hola pepe!"),
    path('indice', views.indice, name='indice'),
     path('indice/<str:nombre>', views.indiceParam, name='indiceParam'),
    path('<str:nombre>', views.holaTu, name='Hola Tu!')
]