from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^historial/$','principal.views.lista_historial'),
    url(r'^historial/(?P<id_historial>\d+)$','principal.views.detalle_historial'),
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^comentario/$','principal.views.nuevo_comentario'),
    url(r'^historial/nuevo/$','principal.views.nuevo_historial'),
    url(r'^usuario/nuevo/$','principal.views.nuevo_usuario'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^privado/$','principal.views.privado'),
    url(r'^cerrar/$','principal.views.cerrar'),
    
    ######################newapp    
    (r"^mark_done/(\d*)/$", "newapp.views.mark_done"),
   
   
    
    
)