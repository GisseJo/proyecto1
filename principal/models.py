from django.db import models

class Persona (models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.TextField(max_length=50)
	CI = models.TextField(max_length=50)

	def __unicode__(self):
		return self.nombre
