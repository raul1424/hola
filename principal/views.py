from django.shortcuts import render
from django.http import HttpResponse

def holaDjango(request):
    return HttpResponse("<h1>Hola Django!</h1>")

def pepe(request):
    return HttpResponse("<h1>Hola pepe!</h1>")