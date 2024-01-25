# Simple API for a login, registration and dashboard app


## Basic description
Backend built with django and django-rest-framework. Authentication and registration services for users already implemented. In this api, the data is auto-generated in the backend --> according to the data it creates a whole graphic and is sent through the api as a base64-uri ready to be consumed by the frontend client in the dashboard!! 

## Lenguajes Utilizados

- Backend: Python a travez de su framework más famoso: Django. La considere perfecta para el proyecto ya que una de sus herramientas (Django Rest Framework) trae la logica para crear una API REST de manera sencilla y facilita el proceso de autenticación
- Para generar la gráfica: Use la libreria matplotlib de python. A travez de esta se lee el modelo de 'data' y se genera la gráfica como una imagen que se envía al cliente junto con la data mediante base64 (una imagen) en el mismo pedido JSON.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de carpetas:

-  proyecto api y aplicacion api_rest

## Para probarlo



```
pip install -r requirements.txt
source Scripts/activate
python manage.py runserver
```

