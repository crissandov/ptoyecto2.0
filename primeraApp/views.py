from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def primeravista(request):
    return HttpResponse("<h1>prueba 1</h1>")

def segundavista(request):
    return HttpResponse("<h1>prueba 2</h1>")
