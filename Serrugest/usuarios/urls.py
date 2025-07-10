from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('dashboard/', views.dashboard_admin, name='dashboard_admin'),

]
