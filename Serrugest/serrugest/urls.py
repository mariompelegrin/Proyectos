from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios import views as usuarios_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('almacen/', include('almacen.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('accounts/logout/', usuarios_views.cerrar_sesion, name='logout'),  
    path('', auth_views.LoginView.as_view(template_name='usuarios/login.html')),  # ruta raíz al login
]



