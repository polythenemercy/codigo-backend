#Reto 2: Ingresar Personas
# - Capture cuantas Personas vamos a ingresar
# - Pedir su nombre, dni y fecha de nacimiento 
# - mostrarlas en un orden de la mas joven a la mas adulta

#Declaración de variables:
value = int(input("¡Ingrese el numero de personas a registrar!: "))
data_reg = []

if value <= 0:

  print("¡Valor registrado incorrecto!") 

else:

  #Procedimiento - Recorrer rango:
  for n in range(value):

    #Declaración de variables:
    name_reg = input("¡Ingrese su nombre!: ")
    id_reg = int(input("¡Ingrese su D.N.I.!: "))
    date_reg = input("¡Ingrese su fecha de nacimiento! (AAAA-MM-DD): ")

    #Procedimiento - Incluir en arreglo:
    data_reg.append({
      'name_reg': name_reg, 
      'id_reg': id_reg, 
      'date_reg': date_reg
    })

  #Procedimiento - Crear arreglo en nuevo orden:
  data_reg_s = sorted(
      data_reg, key=lambda data: data['date_reg'], reverse=True)

  for i, data_reg_s in enumerate(data_reg_s):

    print(data_reg_s['name_reg'])