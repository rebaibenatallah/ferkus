from django import forms
from .models import Tarjama,Contact,art_mois,image_art

class Tarjama_form(forms.ModelForm):
    class Meta:
        model =Tarjama
        fields = '__all__'

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class article_mois_form(forms.ModelForm):
    class Meta:
        model = art_mois
        fields = '__all__'

