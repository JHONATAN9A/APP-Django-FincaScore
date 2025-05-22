from django import forms
from .models import FincaRecordModel, ExperienciaModel, EvaluacionFinca
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
            'biografia_propietario',
            'descripcion'
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
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción general de la finca (paisaje, ambiente, servicios, etc.)'
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

class EvaluacionFincaForm(forms.ModelForm):
    class Meta:
        model = EvaluacionFinca
        fields = [
            # Agrícola
            'infraestructura', 'manejo_agua', 'fertilizacion', 'control_plagas',
            'variedades_cafe', 'asociacion_cultivos', 'rotacion_cultivos',

            # Forestal
            'cobertura_forestal', 'cercas_vivas', 'preservacion_bosque', 'uso_plantas_nativas',

            # Hídrico
            'recoleccion_agua_lluvia', 'conservacion_fuentes', 'sistemas_riego', 'tratamiento_aguas_residuales',

            # Socioeconómico
            'participacion_comunitaria', 'asistencia_tecnica', 'formalizacion_laboral',
            'educacion_caficultor', 'uso_tecnologia',

            # Sostenibilidad
            'uso_insumos_ecologicos', 'gestion_residuos',

            # Comentario
            'comentario'
        ]

        widgets = {
            **{
                field: forms.Select(
                    choices=[(i, str(i)) for i in range(1, 6)],
                    attrs={'class': 'form-select'}
                )
                for field in fields if field != 'comentario'
            },
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Observaciones generales sobre la finca...'
            })
        }

