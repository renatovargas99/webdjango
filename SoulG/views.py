from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'SoulG/index.html')


def Aventura(request):
    return render(request, 'SoulG/Aventura.html')

