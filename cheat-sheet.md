- Crear un entorno virtual:
-> python -m venv env

1- Iniciar el entorno virtual desde Win 10:
-> Set-ExecutionPolicy Unrestricted -Scope Proces
-> .\activate.ps1

- Desactivar el entorno virtual desde Win 10:
-> deactivate

2- Instalar dependencias:
-> pip install -r requirements.txt

3- Crear proyecto de Django:
-> django-admin startproject todolist

4- Inicializar proyecto Django [Desde carpeta de proyecto]:
-> python manage.py startapp 'app'

5- Iniciar servidor local:
-> python manage.py runserver

6- Registrar 'app' en proyecto_nombre/settings.py en arreglo "INSTALLED_APPS"

7- Definir modelo en 'app'/models.py, crear clase y definir atributos y tipo de datos del modelo

8- Realizar migración 
-> python manage.py makemigrations

9- Ejecutar migración 
-> python manage.py migrate

project/settings.py -> Se define la aplicación
app/models.py       -> Se define el modelo
app/views.py        -> Se definen las vistas
project/urls.py     -> Se definen las rutas