from django import forms
from django.db import models



class Jugador(models.Model):
    nombre=models.CharField(max_length=80)
    edad=models.IntegerField()

class Estadisticas(models.Model):
    goles=models.IntegerField()
    asistencias=models.IntegerField()

class Equipo(models.Model):
    equipo=models.CharField(max_length=80)
    







      
# Create your models here.
