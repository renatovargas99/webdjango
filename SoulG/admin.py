from django.contrib import admin
from.models import Categoria, Juego, Cliente, Trabajador, Proveedor, Compra, Reclamo 

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Juego)
admin.site.register(Cliente)
admin.site.register(Trabajador)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(Reclamo)
