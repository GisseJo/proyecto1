from django.contrib import admin
from principal.models import *
from userprofile.models import ContratoAutoeducacion, Perfil

class ContratoAutoeducacionAdmin(admin.ModelAdmin):
    list_display = [ "user", "afirmar", "liberar", "adquirir",]
    search_fields = [ "proposito"]

admin.site.register(ContratoAutoeducacion, ContratoAutoeducacionAdmin)




admin.site.register(Perfil )

