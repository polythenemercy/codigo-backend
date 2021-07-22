# Reto 3: Desarrollo de Productos con POO
# Tener un programa que reciba una cantidad de productos a ingresar, 
# que luego de ingresarlos (instanciar) podamos llamar a uno de ellos y que nos muestre su descripción 
# y si no, tengamos una opción para terminar el programa. (Usar if elif else y while)

class Producto:

  def __init__ (self, sku, description):

    self.sku = sku
    self.description = description

#Declaración de variables:
value = int(input("¡Ingrese el numero de productos a registrar!: "))
data_reg = []

if value > 0:

  #Procedimiento - Recorrer rango:
  for n in range(value):

    product = Producto(input("¡Ingresar código SKU!"), input("¡Ingresar descripción del artículo!"))
    data_reg.append(product)

  print(data_reg)
else:

  print("¡Valor registrado incorrecto!") 

