from django import forms
from .models import Tarjama

class Tarjama_form(forms.ModelForm):
    class Meta:
        model =Tarjama
        fields = '__all__'
