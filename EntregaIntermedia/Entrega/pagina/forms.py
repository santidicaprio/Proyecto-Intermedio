
from django import forms
from django.db import models

class JugadorForm(forms.Form):
    nombre=forms.CharField(max_length=80)
    edad=forms.IntegerField()

class EstadisticasForm(forms.Form):
    goles=forms.IntegerField()
    asistencias=forms.IntegerField()

class EquipoForm(forms.Form):
    equipo=forms.CharField(max_length=80),