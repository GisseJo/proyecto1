from principal.models import Persona, historial, comentario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from django.core.mail import EmailMessage
from principal.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#,context_instance=RequestContext(request) esto hace que se puedan acceder a los paths de settings y demas

def lista_personas(request):
	personas= Persona.objects.all()
	return render_to_response('lista_personas.html',{'lista':personas},context_instance=RequestContext(request))

def sobre(request):
	html = "<html><body>Estamos experimentando</body></html>"
	return HttpResponse(html)

def inicio(request):
	historials = historial.objects.all()
	return render_to_response('inicio.html',{'historials':historials},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def usuarios (request):
	usuarios= User.objects.all()
	historiales = historial.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios,'historiales':historiales },context_instance=RequestContext(request))

def detalle_historial (request, id_historial):
	dato = get_object_or_404(historial, pk=id_historial)
	comentarios = comentario.objects.filter(historial=dato)
	return render_to_response ('historial.html', {'historial':dato, 'comentarios':comentarios }, context_instance=RequestContext(request))
def lista_historial(request):
	historiales=historial.objects.all()
	return render_to_response('historiales.html', {'datos':historiales},context_instance=RequestContext(request))

def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo ='Mensaje del Historial de Agenvida'
			contenido = formulario.cleaned_data['mensaje']+ "\n"
			contenido += 'Comunicarse a' + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['rodri.valdez@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm()
	return render_to_response('contacto.html', {'formulario':formulario},context_instance=RequestContext(request))

def nuevo_historial(request):
	if request.method=='POST':
		formulario = HistorialForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/historial')
	else:
		formulario = HistorialForm()
	return render_to_response('historialform.html', {'formulario':formulario},context_instance=RequestContext(request))


def nuevo_comentario(request):
	if request.method=='POST':
		formulario = ComentarioForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/historial')
	else:
		formulario = ComentarioForm()
	return render_to_response('comentarioform.html', {'formulario':formulario},context_instance=RequestContext(request))
def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('nuevousuario.html',{'formulario':formulario},context_instance=RequestContext(request))

# vista para ingreso al sistema					
def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))
   
   
@login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	try:
		ua = request.META['HTTP_USER_AGENT']
	except KeyError:
		ua = 'unknown'	
	return render_to_response('privado.html',{'usuario':usuario,'ua':ua },context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')




 
 
 