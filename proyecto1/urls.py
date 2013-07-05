from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *
from blog.models import *
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
  urlpatterns = patterns("blog.views",
   (r"^post/(?P<dpk>\d+)/$"          , PostView.as_view(), {}, "post"),
   (r"^archive_month/(\d+)/(\d+)/$"  , ArchiveMonth.as_view(), {}, "archive_month"),
   (r"^$"                            , Main.as_view(), {}, "main"),
   # (r"^delete_comment/(\d+)/$"       , "delete_comment", {}, "delete_comment"),
)

   
   
    
    
)