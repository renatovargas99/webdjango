from django.shortcuts import render

# Create your views here.
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
