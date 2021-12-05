from django.shortcuts import render
from datetime import datetime

def indice(request):
    return render(request,"viernes/index.html" , {
        'esViernes':datetime.today().isoweekday()==5
    })