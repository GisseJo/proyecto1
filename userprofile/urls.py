from django.conf.urls import patterns, include, url





urlpatterns = patterns('',
 url(r'^profile/$', 'userprofile.views.user_profile'),
 url(r'^contrato/$', 'userprofile.views.contrato_autoeducacion'),
 )