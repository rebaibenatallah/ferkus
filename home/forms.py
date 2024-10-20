from django import forms
from .models import Tarjama,Contact

class Tarjama_form(forms.ModelForm):
    class Meta:
        model =Tarjama
        fields = '__all__'

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'