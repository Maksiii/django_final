from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['plu_codigo','nombre','marca','precio','stock','tipo','imagen','fecha_ingreso','fecha_modificacion']

    # Para filtrar Listado
    #search_field = ['plu_codigo','nombre']
    #list_per_page = 3

class Items_carritoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto','precio_producto','imagen','stock']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id_usuario','nombre','contraseña','fecha_ingreso','fecha_modificacion']

  

admin.site.register(Tipo_producto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Items_carrito,Items_carritoAdmin)
admin.site.register(Usuario,UsuarioAdmin)


