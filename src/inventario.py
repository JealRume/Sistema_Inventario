# ----------------------------------------------------------
# ----------------------------------------------------------
# PROGRAM: INVENTORY SYSTEM 
# ----------------------------------------------------------
# AUTHOR: Jesús Ruiz
# DESCRIPTION: This program allow enter the product name, product price and the quantity in the inventory available.



# Definition of variables 

# Nombre del producto
while True:
    nombre = str(input ("Ingrese nombre del producto:"))
    if nombre.strip() == "":
        print ("Error, el nombre no puede estar vacio, Intente nuevamente.")
    else:
        break

# Precio del producto
while True:
    try:
        precio = float(input ("Ingrese precio del producto:"))
        if precio.__float__() < 0:
         print ("Error, el precio no puede ser negativo")
        else:
         break
    except ValueError: 
     print("Error: Debe ingresar un número valido")


# Cantidad del producto
while True:
    try:
        cantidad = int(input ("Ingrese cantidad del producto:"))
        if cantidad.__int__() < 0:
         print ("Error: la cantidad no puede ser negativa")
        else: 
         break
    except ValueError: 
      print ("Error: Debe ingresar un número valido") 

#Calculo de costo total
costo_total =  precio * cantidad 

# Show in console the entered product
print ("====Producto Ingresado====")
print ("Nombre:",nombre)
print ("Precio:",precio)
print ("Cantidad:",cantidad)
print ("Costo Total:",costo_total)