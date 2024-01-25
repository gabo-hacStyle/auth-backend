from rest_framework import serializers
#Trayendo modelos
from .models import User, Data
#Librerias para fechas
from datetime import date, timedelta

#Serializadores para usuarioss
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    #Funcion para crear un nuevo usuario
    def create(self, validated_data):
        #Se crea un nuevo usuario con los datos validados
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

#Serializadores para datos
class DataSerializer(serializers.ModelSerializer):
    #Formato de entrada de fecha
    date = serializers.DateField(input_formats=['%d/%m/%Y'], required=False)

    class Meta:
        model = Data
        fields = ['date', 'value']

    #Funcion para crear un nuevo dato en fecha que sea incrementando uno a uno a la ultima fecha registrada
    def create(self, validated_data):
        if 'date' not in validated_data:
            latest_data = Data.objects.latest('date') if Data.objects.exists() else None
            validated_data['date'] = latest_data.date + timedelta(days=1) if latest_data else date(2024, 1, 1)
        return super().create(validated_data)
