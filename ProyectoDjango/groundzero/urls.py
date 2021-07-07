from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-proveedores', views.ver_proveedores, name='ver-proveedores'),
    path('registrar-proveedor', views.registrar_proveedor, name='registrar-proveedor'),
    path('modificar-proveedor/<id>', views.modificar_proveedor, name='modificar-proveedor'),
    path('eliminar-proveedor/<id>', views.eliminar_proveedor, name='eliminar-proveedor')
]