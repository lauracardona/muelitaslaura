from django.urls import path

from . import views

app_name = 'Muelitas'
urlpatterns = [
    
    path('inicio/<str:msn>/', views.index, name='inicio'),
    path('principal/', views.principal, name='principal'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('formularioLogin/', views.formularioLogin, name='formularioLogin'),
    path('formularioRegistro/', views.formularioRegistro, name='formularioRegistro'),
    path('usuarioGuardar/', views.usuarioGuardar, name='usuarioGuardar'),
]