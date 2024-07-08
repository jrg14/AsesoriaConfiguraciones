from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Ensamblador/", views.ensamblador, name="ensamblador"),
    path("Configuraciones/", views.configuraciones, name="configuraciones"),
    path("PanelControl/", views.panelControl, name="panelControl"),
    path("DatosUsuario/", views.DatosUsuario, name="DatosUsuario"),
    path("Contactar/", views.Contactar , name="Contactar"),
    path("Incidencias/", views.Incidencias , name="Incidencias"),    
    path("About/", views.about , name="about"),    
        
]