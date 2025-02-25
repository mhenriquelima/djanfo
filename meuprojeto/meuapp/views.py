from django.shortcuts import render
from django.http import HttpResponse

def morra(request):
    return render(request,"meuapp/morra.html")
def busque(request):
    return render(request,"meuapp/busque.html")
