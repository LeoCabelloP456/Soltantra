from django.urls import path
from . import views


urlpatterns = [
    #Paths del core
    path('', views.home, name="home"),
    path('masajes_hombresnv1/', views.masajes_hombresnv1, name="masajes_hombresnv1"),
    path('masajes_hombresnv2/', views.masajes_hombresnv2, name="masajes_hombresnv2"),
    path('masajes_hombresnv3/', views.masajes_hombresnv3, name="masajes_hombresnv3"),
    path('masajes_mujeresnv1/', views.masajes_mujeresnv1, name="masajes_mujeresnv1"),
    path('masajes_mujeresnv2/', views.masajes_mujeresnv2, name="masajes_mujeresnv2"),
    path('masajes_mujeresnv3/', views.masajes_mujeresnv3, name="masajes_mujeresnv3"),
    path('masajes_parejasguiado/', views.masajes_parejasguiado, name="masajes_parejasguiado"),
    path('masajes_parejassimultaneo/', views.masajes_parejassimultaneo, name="masajes_parejassimultaneo"),
    path('clases/', views.clases, name="clases"),
    path('clases_individuales/', views.clases_individuales, name="clases_individuales"),
    path('clases_online/', views.clases_online, name="clases_online"),
    path('clases_pareja/', views.clases_pareja, name="clases_pareja"),
    path('clases_video/', views.clases_video, name="clases_video"),
    path("videos/", views.video_list, name="video_list"),
    path("videos/<slug:slug>/", views.video_detail, name="video_detail"),
    path('practicas/', views.practicas, name="practicas"),
    path('talleres/', views.talleres, name="talleres"),
    path('staff/', views.staff_list, name="staff_list"),
    path('tienda/', views.tienda, name="tienda"),  
    path('reserva_online/', views.reserva_online, name="reserva_online"),
    path('social/', views.social, name="social"),
    path('page/', views.page, name="page"),
    path('reclutar/', views.reclutar, name="reclutar"),
    path('contact/', views.contact, name="contact"),
    path("cart/", views.cart_detail, name="cart_detail"), 
    path("add_to_cart/<slug:slug>/", views.add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<slug:slug>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/update/<str:slug>/", views.update_cart, name="update_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("apply-coupon/", views.apply_coupon, name="apply_coupon"),
    path("staff/<slug:slug>/", views.staff_detail, name="staff_detail"),
]
