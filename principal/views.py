from django.shortcuts import render
from django.http import HttpResponse

def holaDjango(request):
    return HttpResponse("<h1>Hola Django!</h1>")

def pepe(request):
    return HttpResponse("<h1>Hola pepe!</h1>")

def holaTu(request, nombre):
    return HttpResponse(f'<h1>Hola {nombre.capitalize()}!</h1>')

def indice(request):
    return render(request,"principal/index.html")

def indiceParam(request, nombre):
    return render(request, 'principal/saludo.html', {'nombre':nombre.capitalize()})