from django import forms
from .models import *

class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'ano_lectivo': forms.NumberInput(attrs={'class': 'form-control'}),
            'alumno': forms.Select(attrs={'class':'form-control'}),
            'nivel': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'})
        }
        #roll_no = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Roll', 'class': 'form-control'}))
