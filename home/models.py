from django.db import models
from django.contrib import admin

# Create your models here.
class Tarjama(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    # date = models.DateField(null=True)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    required = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


admin.site.register(Tarjama)
admin.site.register(Contact)
