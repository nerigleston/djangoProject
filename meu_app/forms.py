from django import forms
from .models import Dado


class DadoForm(forms.ModelForm):
    class Meta:
        model = Dado
        fields = ['nome', 'idade']
