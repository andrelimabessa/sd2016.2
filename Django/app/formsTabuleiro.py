from django import forms
from .models import Posicao

class TabuleiroForm(forms.ModelForm):
    
    class Meta:
        model = Posicao
        fields = ()
