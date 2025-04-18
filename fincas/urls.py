from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .views import logout_view


urlpatterns = [
    path('', views.lista_fincas, name='inicio'),
    path('finca/<int:finca_id>/editar/', views.editar_finca, name='editar_finca'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('panel-fincas/', views.panel_fincas, name='panel_fincas'),
    path('registrar-finca/', views.registrar_finca, name='registrar_finca'),
    path('editar-finca/<int:finca_id>/', views.editar_finca, name='editar_finca'),
    path('eliminar-finca/<int:finca_id>/', views.eliminar_finca, name='eliminar_finca'),
    path('detalle-finca/<int:finca_id>/', views.detalle_finca, name='detalle_finca'),
    path('detalle-experiencias/<int:finca_id>/', views.detalle_experiencias, name='detalle_experiencias'),
    path('finca/<int:finca_id>/experiencias/', views.detalle_experiencias, name='detalle_experiencias'),
    path('finca/<int:finca_id>/agregar-experiencia/', views.agregar_experiencia, name='agregar_experiencia'),
    path('experiencia/<int:experiencia_id>/editar/', views.editar_experiencia, name='editar_experiencia'),
    path('experiencia/<int:experiencia_id>/eliminar/', views.eliminar_experiencia, name='eliminar_experiencia'),
    
    

        
    # Password reset
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             email_template_name='password_reset_email.html',
             subject_template_name='password_reset_subject.txt'
         ), 
         name='password_reset'),
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ), 
         name='password_reset_complete'),
]
