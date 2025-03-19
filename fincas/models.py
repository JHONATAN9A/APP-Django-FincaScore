from django.db import models


class FincaRecordModel(models.Model):
    lugar = models.CharField(max_length=255)  
    propietario = models.CharField(max_length=255)  
    fotografias = models.ImageField(upload_to='static/img/fincas/', blank=True, null=True)

    class Meta:
        db_table = 'finca_record'
        verbose_name = 'Registro Finca'
        verbose_name_plural = 'Registros Fincas'  

    def __str__(self):
        return f"{self.lugar} - {self.propietario}"
