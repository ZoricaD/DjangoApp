from django import forms

from polls.models import Produkt


class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = '__all__'
        exclude = ['user']