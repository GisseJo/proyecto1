#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc

class Persona (models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.TextField(max_length=50)
	CI = models.TextField(max_length=50)

	def __unicode__(self):
		return self.nombre

class historial(models.Model):
	ideal_personal = models.TextField(unique=True, max_length=100)
	nombre_de_grupo = models.CharField(max_length=100)
	historia = models.TextField(help_text= 'Comenta tus pasos en Schoenstatt')
	imagen_de_perfil = models.ImageField(upload_to = 'fotos', verbose_name='Image')
	tiempo_de_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.ideal_personal

class comentario (models.Model):
	historial = models.ForeignKey(historial)
	texto = models.TextField(help_text='Escribi pues algo', verbose_name='comentario')

	def __unicode__(self):
		return self.texto


class WorkoutCalendar(HTMLCalendar):

    def __init__(self, workouts):
        super(WorkoutCalendar, self).__init__()
        self.workouts = self.group_by_day(workouts)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.workouts:
                cssclass += ' filled'
                body = ['<ul>']
                for workout in self.workouts[day]:
                    body.append('<li>')
                    body.append('<a href="%s">' % workout.get_absolute_url())
                    body.append(esc(workout.title))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(WorkoutCalendar, self).formatmonth(year, month)

    def group_by_day(self, workouts):
        field = lambda workout: workout.performed_at.day
        return dict(
            [(day, list(items)) for day, items in groupby(workouts, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)


