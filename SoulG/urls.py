from django.http import HttpResponse
from django.urls import path
from .views import (index, Aventura, Combate, Deporte , Rol , Terror , Registro , Inicio_Session , Carrito , AcM , Adinfinitum, Diablo, Easport, RE4, RecContrasena, 
                   Session, SF6, Starfield, SWfw, WWE, Juego_lista, Juego_editar)
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return HttpResponse("invalido")

urlpatterns = [
    path('Juego_editar/<id>', Juego_editar, name='Juego_editar'),
    path('Juego_lista', Juego_lista, name='Juego_lista'),
    path('', index, name='index'),
    path('Aventura', Aventura, name='Aventura'),
    path('Combate', Combate, name='Combate'),
    path('Deporte', Deporte, name='Deporte'),
    path('Rol', Rol, name='Rol'),
    path('Terror', Terror, name='Terror'),
    path('Registro', Registro, name='Registro'),
    path('Inicio_Session', Inicio_Session, name='Inicio_Session'),
    path('Carrito', Carrito, name='Carrito'),
    path('AcM', AcM, name='AcM'),
    path('Adinfinitum', Adinfinitum, name='Adinfinitum'),
    path('Diablo', Diablo , name='Diablo'),
    path('Easport', Easport, name='Easport'),
    path('RE4', RE4, name='RE4'),
    path('RecContrasena', RecContrasena, name='RecContrasena'),
    path('Session', Session, name='Session'),
    path('SF6', SF6, name='SF6'),
    path('Starfield', Starfield, name='Starfield'),
    path('SWfw', SWfw, name='SWfw'),
    path('WWE', WWE, name='WWE'),

]