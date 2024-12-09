from django.http import HttpResponse
from django.shortcuts import render
from .models import Marcas

# Create your views here.
def index(request):
    return HttpResponse("hola mundo")

def cotizar (request):
    marcas = Marcas.objects.all()
    return render(request, "cotizar.html",{
        "marcas": marcas,
    })