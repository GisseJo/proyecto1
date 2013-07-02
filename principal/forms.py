#enconding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import historial , comentario


class ContactoForm (forms.Form):
    correo = forms.EmailField(label='Tu correo electronico')
    mensaje = forms.CharField(widget=forms.Textarea)
    
class HistorialForm(ModelForm):
    class Meta:
        model = historial
        
class ComentarioForm(ModelForm):
    class Meta:
        model = comentario