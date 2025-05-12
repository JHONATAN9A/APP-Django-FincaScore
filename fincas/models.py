from django.db import models
from django.contrib.auth.models import User

class FincaRecordModel(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lugar = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    fotografias = models.ImageField(upload_to='static/img/fincas/', blank=True, null=True)
    tiene_parqueadero = models.BooleanField(default=False)
    tiene_restaurante = models.BooleanField(default=False)
    experiencias = models.TextField(
        help_text="Describe brevemente las experiencias ofrecidas",
        null=True, blank=True
    )
    costo_experiencia = models.CharField(
        max_length=255,
        help_text="Ejemplo: $30.000 por persona o Ingreso gratuito",
        null=True, blank=True
    )
    biografia_propietario = models.TextField(
        help_text="Una breve reseña del propietario",
        null=True, blank=True
    )

    class Meta:
        db_table = 'finca_record'
        verbose_name = 'Registro Finca'
        verbose_name_plural = 'Registros Fincas'
    

    def __str__(self):
        return f"{self.lugar} - {self.propietario.username}"

class ExperienciaModel(models.Model):
    finca = models.ForeignKey(FincaRecordModel, on_delete=models.CASCADE, related_name='experiencias_finca')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    actividad = models.TextField(help_text="Describe qué se hace en esta experiencia.")
    imagen = models.ImageField(upload_to='static/img/experiencias/', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.finca.lugar}"