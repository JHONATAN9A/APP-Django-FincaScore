from django.shortcuts import render, get_object_or_404, redirect
from fincas.models import FincaRecordModel
from django.http import Http404

def HomeView(request):
    return render(request, 'index.html')

def MasDetalles(request, finca_id):
    try:
        finca = FincaRecordModel.objects.get(id=finca_id)
    except FincaRecordModel.DoesNotExist:
        raise Http404("No existe ninguna finca con ese ID")

    return render(request, 'MasDetalles.html', {'finca': finca})

def AboutView(request):
    return render(request, 'about.html')

def Contacto(request):
    return render(request, 'Contacto.html')