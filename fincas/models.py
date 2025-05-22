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
    descripcion = models.TextField(help_text="Descripción general de la finca", null=True, blank=True)

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

class EvaluacionFinca(models.Model):
    finca = models.ForeignKey(FincaRecordModel, on_delete=models.CASCADE, related_name='evaluaciones')
    evaluador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    # Componente Agrícola
    infraestructura = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    manejo_agua = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    fertilizacion = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    control_plagas = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    variedades_cafe = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    asociacion_cultivos = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    rotacion_cultivos = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    # Componente Forestal
    cobertura_forestal = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    cercas_vivas = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    preservacion_bosque = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    uso_plantas_nativas = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    # Componente Hídrico
    recoleccion_agua_lluvia = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    conservacion_fuentes = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    sistemas_riego = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    tratamiento_aguas_residuales = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    # Componente Socioeconómico
    participacion_comunitaria = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    asistencia_tecnica = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    formalizacion_laboral = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    educacion_caficultor = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    uso_tecnologia = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    # Sostenibilidad y Medio Ambiente
    uso_insumos_ecologicos = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    gestion_residuos = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    # Observaciones
    comentario = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('finca', 'evaluador')

    def puntaje_total(self):
        campos = [
            self.infraestructura, self.manejo_agua, self.fertilizacion, self.control_plagas,
            self.variedades_cafe, self.asociacion_cultivos, self.rotacion_cultivos,
            self.cobertura_forestal, self.cercas_vivas, self.preservacion_bosque, self.uso_plantas_nativas,
            self.recoleccion_agua_lluvia, self.conservacion_fuentes, self.sistemas_riego, self.tratamiento_aguas_residuales,
            self.participacion_comunitaria, self.asistencia_tecnica, self.formalizacion_laboral,
            self.educacion_caficultor, self.uso_tecnologia,
            self.uso_insumos_ecologicos, self.gestion_residuos
        ]
        return round(sum(campos) / len(campos), 2)

    def __str__(self):
        return f"{self.finca.lugar} - {self.evaluador.username}"


