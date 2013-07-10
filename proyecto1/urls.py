#encoding:utf-8
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
    
    ######################newapp´-TODO    
    (r'^mark_done/(\d*)/$', 'newapp.views.mark_done'),

    ###################blog
    url (r'^blog/$','blog.views.main'),
    url (r'^blog/post/(\d+)/$','blog.views.post'),
    url(r'^blog/add_comment/(\d+)/$', 'blog.views.add_comment'),
    url(r"^blog/month/(\d+)/(\d+)/$", 'blog.views.month'),
    url(r"^blog/delete_comment/(\d+)/$", "blog.views.delete_comment"),
    url(r"^blog/delete_comment/(\d+)/(\d+)/$", "blog.views.delete_comment"),

##################CALENDAR
    
    url(r"^cal/(\d+)/$", "cal.views.main"), 
    url(r"^cal/$", "cal.views.main"),

    url(r"^cal/month/(\d+)/(\d+)/(prev|next)/$", "cal.views.month"),
    url(r"^cal/month/(\d+)/(\d+)/$", "cal.views.month"),
    url(r"^cal/month/$", "cal.views.month"),
    url(r"^cal/day/(\d+)/(\d+)/(\d+)/$", "cal.views.day"),
    url(r"^accounts/", include('registration.urls')),
    url(r"^cal/settings/$", "cal.views.settings"),
   
###################FORUM

    url(r"forum/$", "forum.views.main"),
    url(r"^forum/forum/(\d+)/$", "forum.views.forum"),
    url(r"^forum/thread/(\d+)/$", "forum.views.thread"),
    url(r"^forum/post/(new_thread|reply)/(\d+)/$", "forum.views.post"),
    url(r"^forum/reply/(\d+)/$", "forum.views.reply"),
    url(r"^forum/new_thread/(\d+)/$", "forum.views.new_thread"),
    url(r"^forum/profile/(\d+)/$", "forum.views.profile"),
    url(r"^forum/accounts/", include('registration.urls')),

#####################PHOTO

    url(r"^photo/$", "photo.views.main"),
    url(r"^photo/search/$", "photo.views.search"),
    url(r"^photo/(\d+)/$", "photo.views.album"),
    url(r"^photo/image/(\d+)/$", "photo.views.image"),
    url(r"^photo/(\d+)/(full|thumbnails|edit)/$", "photo.views.album"),
)