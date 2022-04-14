from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def estadistica(request):
    return render(request, 'tienda/estadistica.html')

def confirmacion(request):
    return render(request, 'tienda/confirmacion.html')
