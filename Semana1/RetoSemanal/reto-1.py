#Reto 1: Desarrollar un programa de bienvenida
# - Ingresar un nombre y su edad.
# - Si es menor de edad que indique que dependiendo de la hora (si es mas de las 6pm) debe ir a dormir y si no hacer la tarea.
# - Si es mayor de edad que indique que no esta obligado a hacer nada.

#Importar referencia:
import datetime

#Declaración de variables:
name = input("¡Ingrese su nombre!: ")
age = int(input("¡Ingrese su edad!: "))

#Establecer condición - Validar edad:
if age < 18:

  #Establecer condición - Comparar hora actual con parametro definido:
  if datetime.datetime.now().strftime('%H:%M:%S') > '18:00:00':
    
    #Procedimiento - Establecer notificación:
    print("¡", name, " debes ir a dormir!")
  
  else:
    
    #Procedimiento - Establecer notificación:
    print("¡", name, " debes hacer la tarea!")

else:
  
  #Procedimiento - Establecer notificación:
  print("Hola, ", name, "¡Continua!")
