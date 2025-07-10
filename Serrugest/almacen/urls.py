# almacen/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('material/registrar/', views.registrar_material, name='registrar_material'),
    path('entrada/registrar/', views.registrar_entrada, name='registrar_entrada'),
]
