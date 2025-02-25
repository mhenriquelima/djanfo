from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    return render(request,"meuapp/home.html")
def hello(request):
    name = request.POST.get('name')
    if name:
        return render(request,'meuapp/hello.html', {'name': name})
    return render(request,'meuapp/hello.html')
def ListarMarcas(request):
    marcas = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")
    marcas = marcas.json()
    
    return render(request, 'meuapp/ListaMarcas.html', {'marcas' : marcas})