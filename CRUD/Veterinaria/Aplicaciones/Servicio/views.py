from django.shortcuts import redirect, render
from .models import Servicios

# Create your views here.

def home(request):
    serviciosListados = Servicios.objects.all()
    return render(request, "gestionServicios.html", {"servicios": serviciosListados})

def registrarServicio(request):
    id=request.POST['txtId']
    nombre=request.POST['txtNombre']

    servicio = Servicios.objects.create(id=id, nombre=nombre)
    return redirect('/')

def edicionServicio(request, id):
    servicio = Servicios.objects.get(id=id)
    return render(request, "edicionServicios.html", {"servicio": servicio})

def editarServicio(request):
    id=request.POST['txtId']
    nombre=request.POST['txtNombre']

    servicio = Servicios.objects.get(id=id)
    servicio.nombre = nombre
    servicio.save()

    return redirect('/')

def eliminarServicio(request, id):
    servicio = Servicios.objects.get(id=id)
    servicio.delete()

    return redirect('/')

def gestionServicios(request):
    return redirect('/')