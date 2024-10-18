from django.db import models
from django.contrib import admin

# Create your models here.
class tarjama(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()

admin.site.register(tarjama)
