
# ----------------------------------------------------------
# ----------------------------------------------------------
# PROGRAM: INVENTORY SYSTEM 
# ----------------------------------------------------------
# AUTHOR: Jesús Ruiz
# DESCRIPTION: This program allow enter the product name, product price and the quantity in the inventory available.

# Lista de inventario
inventario = []

# Función del Menú "1."
def agregar_producto():
    nombre = input("nombre del producto:")

    precio = float(input(f"Ingrese precio de '{nombre}':"))

    cantidad = int(input(f"Ingrese cantidad de '{nombre}':"))

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append (producto)
    print(f"Listo '{producto}' agregado exitosamente!")

# Función del Menú "2."
def mostrar_inventario():

    print("\n -- Inventario Actual --")
    if not inventario: 
        print("El inventario está vacío")
    else:
         for p in inventario:
             print(f"producto: {p['nombre']} | precio: ${p['precio']} | cantidad: {p['cantidad']}")

# Función del Menú "3."
def calcular_estadisticas():
    if not inventario:
        print("\n --No hay datos para calcular estadiasticas-- ")
        return 
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    total_unidades = sum(p['cantidad'] for p in inventario)

    print("\n --Estadisticas del inventario--")
    print(f"Valor total acumulado {valor_total:.2f}")
    print(f"Total productos en stock {total_unidades}")
    print(f"Variedad de productos {len(inventario)}")

# Función del Menú "4."
def menu_principal():
    while True:
        print("\n ===== MENÚ DE INVENTARIO =====")
        print("1. Agregar producto.")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")
     
        while True:
            try:    
                opcion = int(input("Seleccione una opcion del 1-4:")) 
                break
            except ValueError:
                print("Ingrese un Número")
    
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            calcular_estadisticas()
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else: 
            print("Opción invalida, intente denuevo")        

# NOTA: Dejo pendiente colocarle los try except y los while True
    
    
    
   
 
    