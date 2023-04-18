from django.shortcuts import get_object_or_404, redirect, render
from .models import Juego

# Create your views here.


#Lista de juegos
def Juego_lista(request):
    Juego=Juego.object.all()
    return render(request, 'Juego_lista.html', {'Juego':Juego})
#Vista para la creacion
def Juego_nuevo(request):
    if request.method == "POST":
        formulario = JuegoForm(request.POST)
        if formulario.is_valid():
            Juego = formulario.save(commit=False)
            Juego.save()
            return redirect('Juego_lista')
    else:
        formulario = JuegoForm()
    return render(request, 'Juego_editar.html', {'formulario': formulario})
#crear una vista para la actualizacion
def Juego_editar(request, id):
    Juego = get_object_or_404(Juego, id)
    if request.method == "POST":
        formulario = JuegoForm(request.POST, instance=Juego)
        if formulario.is_valid():
            Juego = formulario.save(commit=False)
            Juego.save()
            return redirect('Juego_lista')
    else:
        formulario = JuegoForm(instance=Juego)
    return render(request, 'Juego_editar.html', {'formulario': formulario})
#crear una vista para la eliminacion
def Juego_eliminar(request, pk):
    Juego = get_object_or_404(Juego, pk=pk)
    Juego.delete()
    return redirect('Juego_lista')


def index(request):
    return render(request, 'SoulG/index.html')

def Aventura(request):
    return render(request, 'SoulG/Aventura.html')

def Combate(request):
    return render(request, 'SoulG/Combate.html')

def Deporte(request):
    return render(request, 'SoulG/Deporte.html')

def Rol(request):
    return render(request, 'SoulG/Rol.html')

def Terror(request):
    return render(request, 'SoulG/Terror.html')

def Registro(request):
    return render(request, 'SoulG/Registro.html')

def Inicio_Session(request):
    return render(request, 'SoulG/Inicio_Session.html')

def Carrito(request):
    return render(request, 'SoulG/Carrito.html')

def Adinfinitum(request):
    return render(request, 'SoulG/Ad_infinitum.html')

def AcM(request):
    return render(request, 'SoulG/AcM.html')

def Diablo(request):
    return render(request, 'SoulG/Diablo.html')

def Easport(request):
    return render(request, 'SoulG/Easport.html')

def RE4(request):
    return render(request, 'SoulG/RE4.html')

def Session(request):
    return render(request, 'SoulG/Session.html')

def SF6(request):
    return render(request, 'SoulG/SF6.html')

def Starfield(request):
    return render(request, 'SoulG/Starfield.html')

def SWfw(request):
    return render(request, 'SoulG/SWfw.html')

def WWE(request):
    return render(request, 'SoulG/WWE.html')

def RecContrasena(request):
    return render(request, 'SoulG/RecContrasena.html')
