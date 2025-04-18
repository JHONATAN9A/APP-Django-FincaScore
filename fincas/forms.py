from django import forms
from .models import FincaRecordModel, ExperienciaModel
from django.contrib.auth.models import User

ROLES = [
    ('Cliente', 'Cliente'),
    ('Propietario', 'Propietario'),
]


class FincaForm(forms.ModelForm):
    class Meta:
        model = FincaRecordModel
        fields = [
            'lugar',
            'latitud',
            'longitud',
            'fotografias',
            'tiene_parqueadero',
            'tiene_restaurante',
            'experiencias',
            'costo_experiencia',
            'biografia_propietario'
        ]
        widgets = {
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'fotografias': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tiene_parqueadero': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tiene_restaurante': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'experiencias': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe las experiencias que ofrece la finca'
            }),
            'costo_experiencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: $30.000 por persona o Ingreso gratuito'
            }),
            'biografia_propietario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Una breve reseña del propietario'
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        latitud = cleaned_data.get("latitud")
        longitud = cleaned_data.get("longitud")

        if latitud is None or longitud is None:
            raise forms.ValidationError("Debe ingresar las coordenadas geográficas (latitud y longitud) de la finca.")

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    rol = forms.ChoiceField(choices=ROLES, label='Rol')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'rol']

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = ExperienciaModel
        fields = ['titulo', 'descripcion', 'actividad', 'imagen']