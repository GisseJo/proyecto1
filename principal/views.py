from principal.models import Persona
from django.shortcuts import render_to_response

def lista_personas(request):
	personas= Persona.objects.all()
	return render_to_response('lista_personas.html',{'lista':personas})
