from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import FincaRecordModel,ExperienciaModel, EvaluacionFinca, ComentarioFinca
from .forms import FincaForm, RegistroForm,ExperienciaForm,EvaluacionFincaForm, ComentarioFincaForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.db.models import Q  # importar para búsquedas flexibles
from django.template.loader import render_to_string
from django.http import HttpResponse

def lista_fincas(request):
    query = request.GET.get('buscar')
    if query:
        fincas = FincaRecordModel.objects.filter(Q(lugar__icontains=query))
    else:
        fincas = FincaRecordModel.objects.all()
    return render(request, 'index.html', {'fincas': fincas, 'query': query})

def lista_fincas(request):
    fincas = FincaRecordModel.objects.all()  # trae todas las fincas
    return render(request, 'index.html', {'fincas': fincas})

def editar_finca(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, id=finca_id)

    if request.method == 'POST':
        form = FincaForm(request.POST, request.FILES, instance=finca)
        if form.is_valid():
            form.save()
            return redirect('mas_detalles', finca_id=finca.id)
    else:
        form = FincaForm(instance=finca)

    return render(request, 'editar_finca.html', {'form': form, 'finca': finca})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encripta la contraseña
            user.save()

            rol_seleccionado = form.cleaned_data['rol']
            grupo = Group.objects.get(name=rol_seleccionado)
            user.groups.add(grupo)

            # (Opcional) Iniciar sesión automáticamente
            login(request, user)

            return redirect('Home App')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente.")
    return redirect('Home App')

@login_required
def panel_fincas(request):
    user = request.user
    if user.groups.filter(name='Administrador').exists():
        fincas = FincaRecordModel.objects.all()
    else:
        fincas = FincaRecordModel.objects.filter(propietario=user)
    
    return render(request, 'fincas/panel_fincas.html', {'fincas': fincas})

@login_required
def registrar_finca(request):
    if request.method == 'POST':
        form = FincaForm(request.POST, request.FILES)
        if form.is_valid():
            finca = form.save(commit=False)
            finca.propietario = request.user
            finca.save()
            return redirect('panel_fincas')
    else:
        form = FincaForm()
    
    return render(request, 'fincas/registrar_finca.html', {'form': form})

@login_required
def detalle_finca(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, pk=finca_id)
    return render(request, 'fincas/detalle_finca.html', {'finca': finca})

@login_required
def editar_finca(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, pk=finca_id)
    if request.user != finca.propietario and not request.user.is_superuser:
        return redirect('panel_fincas')
    
    experiencias = finca.experiencias_finca.all()

    if request.method == 'POST':
        form = FincaForm(request.POST, request.FILES, instance=finca)
        if form.is_valid():
            form.save()
            return redirect('panel_fincas')
    else:
        form = FincaForm(instance=finca)
    
    return render(request, 'fincas/editar_finca.html', {'form': form, 'finca': finca,'experiencias': experiencias})

@login_required
def eliminar_finca(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, pk=finca_id)
    if request.user == finca.propietario or request.user.is_superuser:
        finca.delete()
    return redirect('panel_fincas')

def detalle_experiencias(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, id=finca_id)
    return render(request, 'fincas/detalle_experiencias.html', {'finca': finca})

@login_required
def agregar_experiencia(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, id=finca_id)

    # Verifica si el usuario es propietario o superusuario
    if not (request.user == finca.propietario or request.user.is_superuser):
        raise Http404("No tienes permiso para agregar experiencias a esta finca.")

    if request.method == 'POST':
        form = ExperienciaForm(request.POST, request.FILES)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.finca = finca
            experiencia.save()
            return redirect('detalle_experiencias', finca_id=finca.id)
    else:
        form = ExperienciaForm()

    return render(request, 'fincas/agregar_experiencia.html', {'form': form, 'finca': finca})

@login_required
def detalle_experiencias(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, id=finca_id)
    experiencias = finca.experiencias_finca.all()
    return render(request, 'fincas/detalle_experiencias.html', {'finca': finca, 'experiencias': experiencias})

@login_required
def editar_experiencia(request, experiencia_id):
    experiencia = get_object_or_404(ExperienciaModel, id=experiencia_id)
    finca = experiencia.finca  # <--- extraemos finca

    if request.user != finca.propietario and not request.user.is_superuser:
        return redirect('panel_fincas')

    if request.method == 'POST':
        form = ExperienciaForm(request.POST, request.FILES, instance=experiencia)
        if form.is_valid():
            form.save()
            return redirect('detalle_experiencias', finca_id=finca.id)
    else:
        form = ExperienciaForm(instance=experiencia)

    return render(request, 'fincas/editar_experiencia.html', {
        'form': form,
        'experiencia': experiencia,
        'finca': finca  # <--- agregado al contexto
    })


@login_required
def eliminar_experiencia(request, experiencia_id):
    experiencia = get_object_or_404(ExperienciaModel, id=experiencia_id)

    if request.user != experiencia.finca.propietario and not request.user.is_superuser:
        return redirect('panel_fincas')

    finca_id = experiencia.finca.id
    experiencia.delete()
    return redirect('detalle_experiencias', finca_id=finca_id)

def lista_fincas(request):
    fincas = FincaRecordModel.objects.all()
    print("✔️ Fincas:", fincas)  # Debug temporal
    return render(request, 'index.html', {'fincas': fincas})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Evaluador').exists())
def evaluar_finca(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, id=finca_id)

    evaluacion_existente = EvaluacionFinca.objects.filter(finca=finca, evaluador=request.user).first()

    if request.method == 'POST':
        form = EvaluacionFincaForm(request.POST, instance=evaluacion_existente)
        if form.is_valid():
            evaluacion = form.save(commit=False)
            evaluacion.finca = finca
            evaluacion.evaluador = request.user
            evaluacion.save()
            return redirect('fincas_para_evaluar')  
    else:
        form = EvaluacionFincaForm(instance=evaluacion_existente)

    return render(request, 'evaluador/evaluar_finca.html', {'form': form, 'finca': finca})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Evaluador').exists())
def lista_fincas_para_evaluar(request):
    fincas = FincaRecordModel.objects.all()
    fincas_info = []

    for finca in fincas:
        evaluacion = EvaluacionFinca.objects.filter(finca=finca, evaluador=request.user).first()
        fincas_info.append({
            'finca': finca,
            'evaluada': bool(evaluacion),
            'puntaje': evaluacion.puntaje_total() if evaluacion else None
        })

    return render(request, 'evaluador/fincas_disponibles.html', {'fincas_info': fincas_info})
@login_required
def MasDetalles(request, finca_id):
    finca = get_object_or_404(FincaRecordModel, id=finca_id)

    comentario_existente = ComentarioFinca.objects.filter(finca=finca, usuario=request.user).first()
    comentarios = finca.comentarios.exclude(usuario=request.user).order_by('-fecha_actualizacion')

    if request.method == 'POST':
        form = ComentarioFincaForm(request.POST, instance=comentario_existente)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.finca = finca
            comentario.usuario = request.user
            comentario.save()
            return redirect('mas_detalles', finca_id=finca.id)
    else:
        form = ComentarioFincaForm(instance=comentario_existente)

    return render(request, 'MasDetalles.html', {
        'finca': finca,
        'form_comentario': form,
        'comentarios_usuarios': comentarios,
        'comentario_existente': comentario_existente,
        'rango_estrellas': range(1, 6),
    })
def lista_fincas(request):
    query = request.GET.get('buscar')
    resultados = []

    if query:
        resultados = FincaRecordModel.objects.filter(Q(lugar__icontains=query))

    # Siempre mostrar la galería general
    fincas = FincaRecordModel.objects.all()

    return render(request, 'index.html', {
        'fincas': fincas,
        'query': query,
        'resultados': resultados
    })
def buscar_fincas_parciales(request):
    query = request.GET.get('buscar', '')
    fincas = FincaRecordModel.objects.filter(lugar__icontains=query) if query else []
    html = render_to_string('partials/lista_fincas_resultado.html', {'fincas': fincas})
    return HttpResponse(html)