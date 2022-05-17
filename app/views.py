from django.shortcuts import redirect, render

from .models import *
from .forms import *
# Create your views here.

def index(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    

    return render(request,'app/index.html', datos)

def agregarproducto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente"
    return render(request,'app/productos/agregarproducto.html', datos)

def modificarProductos(request, plu_codigo):
    producto = Producto.objects.get(plu_codigo=plu_codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST,files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto Modifcado correctamente"
            datos['form'] = formulario
    return render(request,'app/productos/modificarProductos.html', datos)

def listarProductos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    


    return render(request,'app/productos/listarProductos.html', datos)

def eliminarProducto(request, plu_codigo):
    producto =Producto.objects.get(plu_codigo=plu_codigo)
    producto.delete()

    return redirect(to="listarProductos")
 


def index_sesion_iniciada(request):
 
    productosAll = Producto.objects.all()
    datos = {'listarProductos' : productosAll}
    
    if request.method == 'POST':
        
        carrito = Items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.stock = request.POST.get('stock_producto')
        carrito.save()



    return render(request,'app/index_sesion_iniciada.html', datos)

def carrito(request):
    carritosAll = Items_carrito.objects.all()
    datos = {
        'listarCarrito' : carritosAll
    }

    

    return render(request,'app/carrito.html', datos)

def segumiento_de_compra(request):
    return render(request,'app/segumiento_de_compra.html')

def historial(request):
    return render(request,'app/historial.html')
    
def crear_usuario(request):
 
    datos = {
        'form' : UsuarioForm()
    }
    if request.method == 'POST' :
        formulario2 = UsuarioForm(request.POST,files=request.FILES)
        if formulario2.is_valid():
            formulario2.save()
            datos['mensaje2'] = "Producto guardado correctamente"
    



    return render(request,'app/crear_usuario.html', datos)
    
def crea_usu(request):
    return render(request,'app/crea_usu.html')

def comprado(request):
    carrito = Items_carrito.objects.all()
    carrito.delete()

    return render(request,'app/comprado.html')

# Usuario #
def listarUsuario(request):
    usuariosAll = Usuario.objects.all()
    datos = {
        'listarUsuarios' : usuariosAll
    }
    
    return render(request,'app/productos/listarUsuario.html', datos)

def modificarUsuario(request, nombre):
    usuario = Usuario.objects.get(nombre=nombre)
    datos = {
        'form' : UsuarioForm(instance=usuario)
    }
    if request.method == 'POST' :
        formulario = UsuarioForm(request.POST,files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto Modifcado correctamente"
            datos['form'] = formulario
    return render(request,'app/productos/modificarUsuario.html', datos)


def eliminarUsuario(request, nombre):
    usuario =Usuario.objects.get(nombre=nombre)
    usuario.delete()

    return redirect(to="productos/listarUsuarios")

def suscribirse(request):
    return render(request,'app/suscribirse.html')

def desuscribirse(request):
    return render(request,'app/desuscribirse.html')

def base_suscrita(request):
    return render(request,'app/suscrito/base_suscrita.html')

def index_suscrito(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }

    if request.method == 'POST':
        
        carrito = Items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.stock = request.POST.get('stock_producto')
        carrito.save()

    
    
    return render(request,'app/suscrito/index_suscrito.html', datos)


def segumiento_suscrito(request):
    
    return render(request,'app/suscrito/segumiento_suscrito.html')

def historial_suscrito(request):
    
    return render(request,'app/suscrito/historial_suscrito.html')

def comprado_suscrito(request):
    carrito = Items_carrito.objects.all()
    carrito.delete()

    
    return render(request,'app/suscrito/comprado_suscrito.html')

def base_sin_carrusel(request):
    
    return render(request,'app/base_sin_carrusel.html')

def base_sin_carru_suscrito(request):
    
    return render(request,'app/suscrito/base_sin_carru_suscrito.html')


def carrito_suscrito(request):
    carritosAll = Items_carrito.objects.all()
    datos = {
        'listarCarrito' : carritosAll
    }

    

    return render(request,'app/suscrito/carrito_suscrito.html', datos)