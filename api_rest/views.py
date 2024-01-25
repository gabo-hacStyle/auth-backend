from rest_framework.response import Response
from rest_framework import status
#Trayendo modelos y serializadores
from .models import User, Data
from .serializers import UserSerializer, DataSerializer
#Trayendo vistas genericas
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
#Trayendo librerias para graficar
import base64
import matplotlib.pyplot as plt
from io import BytesIO


# Create your views here.

class UserListApiView(APIView):
    
    #1. List users

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    #2 Create a new user
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Login como post
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        #authenticate recibe el usuario y la contraseña y devuelve respuesta si es valido
        #libreria de django
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        #Si el usuario es valido, se crea un token de acceso y de refresco
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

#Vista para graficar, get de la data para tabla y grafico
class DataView(APIView):
    def get(self, request):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        plot_base64 = self.plot(data)
        return Response({'data': serializer.data, 'plot': plot_base64}, status=status.HTTP_200_OK)
    #para crear un nuevo dato
    def post(self, request):
        data = Data()
        data.save()
        serializer = DataSerializer(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #para graficar de acuerdo a los datos
    def plot(self, data):
        dates = [d.date for d in data]
        values = [d.value for d in data]
        
        #Grafica de matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(dates, values)
        plt.xlabel('Date')
        plt.ylabel('Value')
        
        #Una imagen y se guarda en un buffer como base64
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_base64 = base64.b64encode(buf.getvalue()).decode()

        return plot_base64

