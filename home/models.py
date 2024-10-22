from django.db import models
from django.contrib import admin

# Create your models here.
class Tarjama(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    # date = models.DateField(null=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    required = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class art_mois(models.Model):
    title = models.CharField(max_length=255)
    data_h = models.CharField(max_length=255,null=True)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class art_mois_tahmich(models.Model):
    text = models.TextField()
    id_art_mois = models.ForeignKey(art_mois,on_delete=models.CASCADE)

class image_art(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    link = models.TextField(null=True)
    def __str__(self):
        return self.name

admin.site.register(art_mois)
admin.site.register(art_mois_tahmich)
admin.site.register(Tarjama)
admin.site.register(Contact)
admin.site.register(image_art)
