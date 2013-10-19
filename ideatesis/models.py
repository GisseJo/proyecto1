from django.db import models

# Create your models here.


class Idea(models.Model):
    user = models.ForeignKey(User, unique=True)
    categoria = models.DateField(null=True)
    tags=models.DateField(null=True)



class Tesis(models.Model):
    tipo= models.DateField(null=True)
    nombre = models.DateField(null=True)

