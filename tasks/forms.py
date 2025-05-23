from django import forms
from .models import Sesion

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['modo_propina']
        widgets = {
            'modo_propina': forms.Select(choices=[('manual', 'Manual'), ('ruleta', 'Ruleta')])
        }
