from django.db import models
from django.contrib import admin

# Create your models here.
class Tarjama(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    # date = models.DateField(null=True)

admin.site.register(Tarjama)
