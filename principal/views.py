#encoding:utf-8
from principal.models import Persona, historial # importa los modelos
from django.shortcuts import render_to_response, get_object_or_404# lanzar error 404
from django.contrib.auth.models import User # importa el modelo usuario de Django
from django.http import HttpResponse, HttpResponseRedirect # Respuesta simple de Http
from django.template import RequestContext #  para poder usar la ruta de las imágenes almacenadas 
#											previamente en la carpeta carga y referenciadas por la url media


def lista_personas(request):
	personas= Persona.objects.all()
	return render_to_response('lista_personas.html',{'lista':personas})
def sobre(request):
	html = "<html><body> Esta pagina web fue creada a modo de pruebas<body><html>"
	return HttpResponse (html)

def	inicio(request):
	Historial= historial.objects.all()
	return render_to_response('inicio.html',{'Historial':Historial})
	
	