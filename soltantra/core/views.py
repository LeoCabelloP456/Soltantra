from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def masajes(request):
    return render(request, "core/masajes.html")

def clases(request):
    return render(request, "core/clases.html")

def practicas(request):
    return render(request, "core/practicas.html")

def masajistas(request):
    return render(request, "core/masajistas.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def reserva(request):
    return render(request, "core/reserva.html")

def tienda(request):
    return render(request, "core/tienda.html")

