from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name="index" ),
    path('index_sesion_iniciada/', index_sesion_iniciada,name="index_sesion_iniciada" ),
    path('segumiento_de_compra/', segumiento_de_compra,name="segumiento_de_compra" ),
    path('historial/', historial,name="historial" ),
    path('carrito/', carrito,name="carrito" ),
    path('agregarproducto/', agregarproducto,name="agregarproducto" ),
    path('modificarProductos/<plu_codigo>/', modificarProductos,name="modificarProductos" ),
    path('eliminarProducto/<plu_codigo>/', eliminarProducto,name="eliminarProducto" ),
    path('listarProductos/', listarProductos,name="listarProductos" ),
    path('comprado/', comprado,name="comprado" ),
    path('crear_usuario/', crear_usuario,name="crear_usuario" ),
    path('crea_usu/', crea_usu,name="crea_usu" ),
    path('listarUsuario/', listarUsuario,name="listarUsuario" ),
    path('modificarUsuario/<nombre>/', modificarUsuario,name="modificarUsuario" ),
    path('eliminarUsuario/<nombre>/', eliminarUsuario,name="eliminarUsuario" ),
    path('suscribirse/', suscribirse,name="suscribirse" ),
    path('desuscribirse/', desuscribirse,name="desuscribirse" ),
    path('base_suscrita/', base_suscrita,name="base_suscrita" ),
    path('index_suscrito/', index_suscrito,name="index_suscrito" ),
    path('carrito_suscrito/', carrito_suscrito,name="carrito_suscrito" ),
    path('historial_suscrito/', historial_suscrito,name="historial_suscrito" ),
    path('segumiento_suscrito/', segumiento_suscrito,name="segumiento_suscrito" ),
    path('comprado_suscrito/', comprado_suscrito,name="comprado_suscrito" ),
    path('base_sin_carrusel/', base_sin_carrusel,name="base_sin_carrusel" ),
    path('base_sin_carru_suscrito/', base_sin_carru_suscrito,name="base_sin_carru_suscrito" ),

]

