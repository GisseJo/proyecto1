from principal.models import Persona, historial, comentario
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.template import RequestContext

def lista_personas(request):
	personas= Persona.objects.all()
	return render_to_response('lista_personas.html',{'lista':personas})

def sobre(request):
	html = "<html><body>Estamos experimentando</body></html>"
	return HttpResponse(html)

def inicio(request):
	historials = historial.objects.all()
	return render_to_response('inicio.html',{'historials':historials})

def usuarios (request):
	usuarios= User.objects.all()
	historiales = historial.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios,'historiales':historiales })

def detalle_historial (request, id_historial):
	dato = get_object_or_404(historial, pk=id_historial)
	comentarios = comentario.objects.filter(historial=dato)
	return render_to_response ('historial.html', {'historial':dato, 'comentarios':comentarios }, context_instance=RequestContext(request))
def lista_historial(request):
	historiales=historial.objects.all()
	return render_to_response('historiales.html', {'datos':historiales},context_instance=RequestContext(request))