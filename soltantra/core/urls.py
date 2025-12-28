from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('masajes/', views.masajes, name="masajes"),
    path('clases/', views.clases, name="clases"),
    path('practicas/', views.practicas, name="practicas"),
    path('masajistas/', views.masajistas, name="masajistas"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('reserva/', views.reserva, name="reserva"),
    path('tienda/', views.tienda, name="tienda"),
]
