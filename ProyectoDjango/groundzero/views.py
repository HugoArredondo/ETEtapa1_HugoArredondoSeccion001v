from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ver_proveedores(request):
    proveedor = Proveedor.objects.all()

    return render(request, 'groundzero/ver_proveedores.html', context={'proveedor':proveedor})

def registrar_proveedor(request):
    if request.method=='POST':
        registro = ProveedorForm(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect('index')
    else:
        registro = ProveedorForm()
    return render(request,'groundzero/registrar_proveedor.html', {'registro':registro})

def modificar_proveedor(request,id):
    registro = Proveedor.objects.get(numIdenti=id)
    datos = {
        'form': ProveedorForm(instance=registro)
    }
    if request.method=='POST':
        formulario = ProveedorForm(data=request.POST, instance = registro)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver-proveedores')
    return render(request, 'groundzero/modificar_proveedor.html', datos)

def eliminar_proveedor(request,id):
    registro = Proveedor.objects.get(numIdenti=id)
    registro.delete()
    return redirect('ver-proveedores')