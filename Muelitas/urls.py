from django.urls import path

from . import views

app_name = 'Muelitas'
urlpatterns = [
    
    path('index/', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('formularioLogin/', views.formularioLogin, name='formularioLogin'),
    path('formularioRegistro/<str:msn>/', views.formularioRegistro, name='formularioRegistro'),
    path('usuarioGuardar/', views.usuarioGuardar, name='usuarioGuardar'),
]