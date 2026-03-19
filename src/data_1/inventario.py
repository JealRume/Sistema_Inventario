
# ----------------------------------------------------------
# ----------------------------------------------------------
# PROGRAM: INVENTORY SYSTEM 
# ----------------------------------------------------------
# AUTHOR: Jesús Ruiz
# DESCRIPTION: This program allow enter the product name, product price and the quantity in the inventory available.

# Lista de inventario
# En esta variable se encuentran todos los diccionarios, es decir cada producto agregado con sus respectivos precios y cantidades.
inventario = []

# Función del Menú "1."
def agregar_producto():
    nombre = input("nombre del producto:")  # No quice colocar condicionales en esta variable debido
                                            # A la variedad de combinaciones entre producto y números.

    while True:       # Este bucle me permite validar si el precio y el valor es positivo, si alguno de los dos no cumple
                      # Automaticamente volverá al menú inicial.
        try:    
            precio = float(input(f"Ingrese precio de '{nombre}':"))
            cantidad = int(input(f"Ingrese cantidad de '{nombre}':"))
            if precio <= 0 or cantidad <= 0:
                print ("Error, los valores asignados deben ser positivos!")
            else:
                producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}         # Aquí se crea un diccionario donde van todos los datos
                inventario.append (producto) #Con esto añadimos la lista al inventario.       # Que anteriormente ingresamos (Nombre, precio y cantidad.)
                print(f"Listo '{producto}' agregado exitosamente!")
                break
        except ValueError:                                         # Esta condicional nos permite validar que los valores ingresados
            print("Error, ingrese un valor numérico")              # Sean netamente numéricos
            

            
        
           
# Función del Menú "2."
def mostrar_inventario():

    print("\n -- Inventario Actual --")           # Título para definir la sección del menú que estamos viendo.
    if not inventario: 
        print("El inventario está vacío")         # Condicional que permite identificar la inexistencia de datos.
    else:
         for p in inventario:
             print(f"*producto: {p['nombre']} | precio: ${p['precio']} | cantidad: {p['cantidad']}")  # Si hay datos se muestran de esta manera.

# Función del Menú "3."
def calcular_estadisticas():          
    if not inventario:
        print("\n --No hay datos para calcular estadiasticas-- ")   # Condicional de inexistencia de datos.
        return 
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario) # Variable de valor total de la suma de productos en stock.
    total_unidades = sum(p['cantidad'] for p in inventario)            # Variable para saber la cantidad de productos en el inventario.

    print("\n --Estadisticas del inventario--")             # Título 
    print(f"Valor total acumulado {valor_total:.2f}")       # Variable 1
    print(f"Total productos en stock {total_unidades}")     # Variable 2
    print(f"Variedad de productos {len(inventario)}")       # Cantidad de diccionarios

# Función del Menú "4."
def menu_principal():
    while True:
        print("\n ==== BIENVENIDO AL INVENTARIO ====")
        print("1. Agregar producto.")
        print("2. Mostrar inventario.")
        print("3. Ver estadisticas.")
        print("4. Salir")
        
        while True:
            try:
                opcion = int(input("Seleccione una opción del 1-4:"))
                break
            except ValueError:
                print("Ingrese un Número")
                
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            calcular_estadisticas
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, intenta nuevamente.")
            
        
        
    # Nota: Finalizado S2M1
    
                    
            
    