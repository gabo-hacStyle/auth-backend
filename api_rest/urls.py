from django.urls import path
from .views import (UserListApiView, LoginView, DataView)

#aqui las urls de la api para ser consumidas por el frontend
urlpatterns = [
    #Ruta para obtener lista de usuarios
    path('users/', UserListApiView.as_view(), name='user-list'),
    #Ruta para login
    path ('login/', LoginView.as_view(), name='login'),
    #Ruta para obtener data y postearla
    path ('data/', DataView.as_view(), name='data'),
    #path('plot/', plot, name='plot'),
]