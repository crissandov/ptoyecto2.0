from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def terceravista(request):
    return HttpResponse("<h1>prueba3</h1>")

def cuartavista(request):
    return HttpResponse("<h1>prueba4</h1>")