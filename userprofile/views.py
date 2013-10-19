# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404 
from django.core.context_processors import csrf
from forms  import UserProfileForm
from forms import ContratoAutoeducacionForm
from models import ContratoAutoeducacion
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance= request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/he')
	else:
		user= request.user
		profile = user.profile
		form = UserProfileForm(instance=profile)
	args = {}
	args.update(csrf(request))
	args['form']= form
	return render_to_response('userprofile/profile.html', args, context_instance=RequestContext(request))

@login_required
def contrato_autoeducacion(request):
	
	if request.method == 'POST':
		contratoAutoeducacionUser = ContratoAutoeducacion(user=request.user)
		form = ContratoAutoeducacionForm(request.POST, instance=contratoAutoeducacionUser)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/he/')
	else:
		contratoAutoeducacionUser = ContratoAutoeducacion.objects.filter(user=request.user);
		contrato = ContratoAutoeducacion.objects.get(id=contratoAutoeducacionUser.id)
		if not 	contratoAutoeducacionUser:
			form =ContratoAutoeducacionForm()
		else:	
			form =ContratoAutoeducacionForm(instance=contratoAutoeducacionUser)
	args = {}
	args.update(csrf(request))
	args['form']= form
	return render_to_response('userprofile/contrato.html', args, context_instance=RequestContext(request))






