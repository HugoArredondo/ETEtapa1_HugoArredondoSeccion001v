from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField, fields_for_model
from django.forms.widgets import Widget
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'numIdenti',
            'photo',
            'nombreProveedor',
            'numContactoProveedor',
            'direccionProveedor',
            'correoProveedor',
            'paisProveedor',
            'contraseña',
            'monedaPago'
        ]
        labels={
            'numIdenti':'Número de Identificación: ',
            'photo':'Fotografía: ',
            'nombreProveedor':'Nombre Completo: ',
            'numContactoProveedor':'Número de Contacto (+569): ',
            'direccionProveedor':'Dirección: ',
            'correoProveedor':'Email: ',
            'paisProveedor':'Pais: ',
            'contraseña':'Contraseña: ',
            'monedaPago':'Moneda de Pago: '
        }
        widgets={
            'numIdenti': forms.TextInput(
                attrs={
                    'id': 'iden',
                    'name': 'iden',
                    'placeholder': '1111',
                    'autofocus': True,
                    'required': True
                }
            ),
            'photo': forms.ClearableFileInput(
                attrs={
                    'id': 'photo',
                    'name': 'photo',
                    'required': True
                }
            ),
            'nombreProveedor': forms.TextInput(
                attrs={
                    'id': 'nom',
                    'name': 'nom',
                    'placeholder': 'Ingrese su Nombre',
                    'required': True
                }
            ),
            'numContactoProveedor': forms.TextInput(
                attrs={
                    'id': 'phone',
                    'name': 'phone',
                    'placeholder': '1111 1111',
                    'autofocus': True,
                    'required': True
                }
            ),
            'direccionProveedor': forms.TextInput(
                attrs={
                    'id': 'adress',
                    'name': 'adress',
                    'placeholder': 'Ingrese su dirección',
                    'autofocus': True,
                    'required': True
                }
            ),
            'correoProveedor': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Ingrese su correo',
                    'autofocus': True,
                    'required': True
                }
            ),
            'paisProveedor': forms.TextInput(
                attrs={
                    'id': 'pais',
                    'name': 'pais',
                    'placeholder': 'Ingrese Pais',
                    'autofocus': True,
                    'required': True
                }
            ),
            'contraseña': forms.PasswordInput(
                attrs={
                    'id': 'password',
                    'name': 'password',
                    'placeholder': 'Ingrese una contraseña',
                    'minlength':'8',
                    'autofocus': True,
                    'required': True
                }
            ),
            'monedaPago': forms.TextInput(
                attrs={
                    'id': 'money',
                    'name': 'money',
                    'placeholder': 'Ingrese medio de pago',
                    'autofocus': True,
                    'required': True
                }
            )
        }
