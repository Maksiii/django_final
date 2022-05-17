from django.db import models

# Create your models here.


class Tipo_producto(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    plu_codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'db_producto'



class Items_carrito(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="Items_carrito", null=True)
    stock = models.IntegerField()


    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'db_Items_carrito'

class Usuario(models.Model):
    id_usuario = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)


    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_Usuario'
