from django import forms
from .models import ObraArte

class ObraArteForm(forms.ModelForm):
    class Meta:
        model = ObraArte
        fields = ['titulo', 'descripcion', 'autor', 'precio', 'imagen','fechaCreacion','vendido', 'galeria']
        

