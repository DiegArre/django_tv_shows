from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Network(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #shows 
    def __str__(self) -> str:
        return self.nombre

    def __repr__(self) -> str:
        return self.nombre

class Show(models.Model):
    titulo = models.CharField(max_length=85)
    network = models.ForeignKey(Network,related_name="shows", on_delete= models.DO_NOTHING)
    release_date = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
