from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gestionServicios', views.gestionServicios),
    path('registrarServicio/', views.registrarServicio),
    path('edicionServicio/<id>', views.edicionServicio),
    path('editarServicio/', views.editarServicio),
    path('eliminarServicio/<id>', views.eliminarServicio)
]