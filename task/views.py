from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def helloworld(request):
    return HttpResponse('El servicio HTTP ha sido iniciado')

def hola_web(request):
    return HttpResponse("Hola Web")

def quien_eres(request):
    return HttpResponse("Soy tu primera app web en arquitectura de SOA")

def que_usas(request):
    return HttpResponse("Estoy construida en el lenguaje de programación Python y utilizo el framework Django")

def mis_datos(request):
    data = {
        "nombreCompleto": "Luis Octavio Lopez Martinez",
        "fechaNacimiento": "2004-01-11",
        "matricula": "220096",
        "edad": 15,
    }
    return JsonResponse(data)