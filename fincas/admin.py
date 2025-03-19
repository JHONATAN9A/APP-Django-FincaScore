from django.contrib import admin
from .models import *

@admin.register(FincaRecordModel)
class FincaRecordAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'propietario') 
    search_fields = ('lugar', 'propietario') 
    list_filter = ('lugar',)
