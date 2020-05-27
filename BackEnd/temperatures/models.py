from django.db import models

# Create your models here.
import uuid

class Temperature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.IntegerField(verbose_name='Latitud del lugar', default=0)
    longitude = models.IntegerField(verbose_name='Longitud del lugar', default=0)
    terrainType= models.TextField(verbose_name='Tipo de terreno',default='')
    value = models.IntegerField(verbose_name='Temperatura(Centigrados)')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)