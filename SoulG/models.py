from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria
    
class Juego(models.Model):
    id_juego=models.AutoField (primary_key=True, max_length=20, verbose_name= 'Id juego')
    nombrejuego = models.CharField(max_length= 20, verbose_name='Nombre videojuego')
    tipojuego = models.CharField(max_length=20, verbose_name= 'Tipo de juego')
    plataformajuego= models.CharField(max_length=50, verbose_name= 'Plataforma juego')

    def __str__(self):
        return self.nombrejuego, self.id_juego
    
    def delete (self, using=None, Keep_parents=False):
        self.id_juego
        super(). delete()
    
class Cliente(models.Model):
    id_cliente=models.AutoField (primary_key=True, max_length=20, verbose_name= 'Id cliente')
    nombre_cliente = models.CharField(max_length= 20, verbose_name='Nombre cliente')
    rut_cliente = models.CharField(max_length=20, verbose_name= 'Rut')
    correo_cliente= models.CharField(max_length=50, verbose_name= 'Correo Cliente')

    def __str__(self):
        return self.id_cliente, self.nombre_cliente
    
    def delete (self, using=None, Keep_parents=False):
        self.id_cliente
        super(). delete()

class Trabajador(models.Model):
    id_trabajador=models.AutoField (primary_key=True, max_length=20, verbose_name= 'Id cliente')
    nombre_trabajador = models.CharField(max_length= 20, verbose_name='Nombre Trabajador')
    rut_trabajador = models.CharField(max_length=20, verbose_name= 'Rut')
    correo_trabajador= models.CharField(max_length=50, verbose_name= 'Correo trabajador')

    def __str__(self):
        return self.id_trabajador, self.nombre_trabajador
    
    def delete (self, using=None, Keep_parents=False):
        self.id_trabajador
        super(). delete()

class Proveedor(models.Model):
    id_proveedor=models.AutoField (primary_key=True, max_length=20, verbose_name= 'Id proveedor')
    nombre_proveedor = models.CharField(max_length= 20, verbose_name='Nombre proveedor')
    rut_proveedor = models.CharField(max_length=20, verbose_name= 'Rut proveedor')
    factura= models.CharField(max_length=50, verbose_name= 'Factura')

    def __str__(self):
        return self.id_proveedor, self.nombre_proveedor
    
    def delete (self, using=None, Keep_parents=False):
        self.id_proveedor
        super(). delete()

class Compra(models.Model):
    id_compra=models.AutoField (primary_key=True, max_length=20, verbose_name= 'Id Compra')
    compra_valor = models.CharField(max_length= 20, verbose_name=' Valor compra')
    id_cliente = models.CharField(max_length=20, verbose_name= 'Id cliente')
    id_videojuego= models.CharField(max_length=50, verbose_name= 'Id videojuego')

    def __str__(self):
        return self.id_compra, self.id_cliente
    
    def delete (self, using=None, Keep_parents=False):
        self.id_compra
        super(). delete()

class Reclamo (models.Model):
    id_reclamo=models.AutoField (primary_key=True, max_length=20, verbose_name= 'Id Reclamo')
    id_usuario = models.CharField(max_length= 20, verbose_name=' Id usuario')
    descripcion = models.TextField(max_length=20, verbose_name= 'descripcion')

    def __str__(self):
        return self.id_reclamo, self.descripcion
    
    def delete (self, using=None, Keep_parents=False):
        self.id_reclamo
        super(). delete()
    
