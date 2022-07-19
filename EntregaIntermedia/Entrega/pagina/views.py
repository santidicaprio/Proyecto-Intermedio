from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from pagina.forms import EquipoForm
from pagina.forms import EstadisticasForm
from pagina.forms import JugadorForm
from pagina.models import Equipo
from pagina.models import Estadisticas
from pagina.models import Jugador

def saludo(request):
	return HttpResponse("Hola, soy Santiago")

def hola(request):
    if request.method == "POST":
        print(request.POST)
        form = JugadorForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            pc = Jugador(
                nombre = cd['nombre'],
                edad = cd['edad']
            
                
            )
            pc.save()
            
            
    return render(request, "pagina/proyecto.html")

def prueba(request):
    context={
        "Jugador":Jugador.objects.all(),
    }
        
    return render(request, "pagina/proyecto.html")

def estadistica(request):
    if request.method == "POST":
        print(request.POST)
        form = EstadisticasForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            pc = Estadisticas(
                goles = cd['goles'],
                asistencias = cd['asistencias']
            
                
            )
            pc.save()
                      
    return render(request, "pagina/estadisticas.html")

def equipo(request):
    if request.method == "POST":
        print(request.POST)
        
        
        
        
            
            
            
    return render(request, "pagina/equipo.html")



# Create your views here.
