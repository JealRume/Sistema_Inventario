# ----------------------------------------------------------
# ----------------------------------------------------------
# PROGRAM: INVENTORY SYSTEM 
# ----------------------------------------------------------
# AUTHOR: Jesús Ruiz
# DESCRIPTION: This program allow enter the product name, product price and the quantity in the inventory available.

import csv
import os
inventario = []

"""Función para agregar un producto"""
def agregar_producto():
    nombre = input("nombre del producto:")  # No quice colocar condicionales en esta variable debido
                                            # A la variedad de combinaciones entre producto y números.
    for p in inventario:
        if p["nombre"].lower() == nombre.lower(): # .lower() ignora mayúsculas/minúsculas
            print("El producto ya se encuentra ingresado.")
            return
    
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
                     
"""Esta función muestra los productos"""
def mostrar_inventario():

    print("\n -- Inventario Actual --")           # Título para definir la sección del menú que estamos viendo.
    if not inventario: 
        print("El inventario está vacío")         # Condicional que permite identificar la inexistencia de datos.
    else:
         for p in inventario:
             print(f"*producto: {p['nombre']} | precio: ${p['precio']} | cantidad: {p['cantidad']}")  # Si hay datos se muestran de esta manera.

"""Esta funcion permite buscar un producto existente"""
def buscar_producto():
    nombre = input("Ingrese nombre del producto que desea encontrar:")
    for p in inventario:
        if p['nombre'].lower() == nombre.lower():
            print(f"Producto encontrado: {p}")
            return p
       
    print("El producto no se encuentra en el inventario.")
    return None

"""Esta función actualiza los valores y cantidades del producto"""
def actualizar_producto():  
    nombre = input("Ingrese producto a actualizar:").strip()
    actualizado = False
    for p in inventario:
        if p['nombre'].strip() == nombre.strip():
            nuevo_precio = float(input("Ingrese nuevo precio:"))
            nueva_canti = int(input("Ingrese nueva cantidad:"))
            p['precio'] = nuevo_precio
            p['cantidad'] = nueva_canti
            print(f"\nRenombrado: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['cantidad']}")
            actualizado = True
            break
    if not actualizado:
        print("Producto no encontrado.")

"""Esta función elimina un producto"""             
def eliminar_producto():
    nombre = input("Ingrese nombre del producto a eliminar:").strip()
    actualizado = False                    
    for p in inventario:
        if p['nombre'].strip() == nombre.strip():
            inventario.remove(p)
            actualizado = True        
            print(f"Producto {nombre} Eliminado.")
    if not actualizado:       
        print("Producto no encontrado.")
            
"""Esta función calcula las estadisticas de los productos que se encuentran en el inventario actual"""
def calcular_estadisticas():          
    if not inventario:
        print("\n --No hay datos para calcular estadiasticas-- ")   # Condicional de inexistencia de datos.
    else:
        valor_total = sum(p['precio'] * p['cantidad'] for p in inventario) # Variable de valor total de la suma de productos en stock.
        total_unidades = sum(p['cantidad'] for p in inventario)   # Variable para saber la cantidad de productos en el inventario.
        producto_mas_caro = max(inventario, key=lambda x: x['precio'])
        producto_mayor_stock = max(inventario, key=lambda x: x['cantidad'])
        print("\n --Estadisticas del inventario--")             # Título 
        print(f"Valor total acumulado {valor_total:.2f}")       # Variable 1
        print(f"Total productos en stock {total_unidades}")
        print(f"Producto mas caro {producto_mas_caro}")
        print(f"Producto con mayor stock {producto_mayor_stock}")
        print(f"Variedad de productos {len(inventario)}")       # Cantidad de diccionarios
 
"""Esta funcion se encarga de guardar los archivos en el csv"""       
def guardar_csv():
    if not inventario:
        print("No hay datos en el inventario para guardar.")
        return
    
    nombre_archivo = input("¿Dónde deseas guardar el archivo? (ej: inventario.csv): ")
    
    # Preguntar el modo de guardado
    print("\nOpciones de guardado:")
    print("1. Sobreescribir el archivo (borra lo anterior)")
    print("2. Añadir al final del archivo")
    opcion = input("Selecciona una opción (1/2): ")
    
    modo = 'w' if opcion == '1' else 'a'
    
    escribir_encabezado = (modo == 'w') or (not os.path.exists(nombre_archivo) or os.stat(nombre_archivo).st_size == 0)

    try: 
        with open(nombre_archivo, mode=modo, newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'precio', 'cantidad']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            if escribir_encabezado:
                escritor.writeheader()
            
            escritor.writerows(inventario)
            
        print(f"¡Inventario guardado exitosamente en modo '{modo}' en {nombre_archivo}!")
    except Exception as e:
        print(f"Ocurrió un error al guardar: {e}")
        
""" Esta función se encarga de cargar un archivo con datos a la memoria del programa"""       
def cargar_csv():
    
    nombre_archivo = input("Escriba el nombre del archivo que desea cargar:")
    try:
        with open(nombre_archivo, mode='r', encoding= 'utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            inventario.clear() 
            
            for fila in lector:
                producto = {
                    "nombre": fila['nombre'],
                    "precio": float(fila['precio']),
                    "cantidad": int(fila['cantidad'])
                }
                inventario.append(producto)
                
        print(f"¡Inventario cargado exitosamente desde {nombre_archivo}!")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe todavía.")
    except Exception as e:
        print(f"Ocurrió un error al cargar: {e}")        
        
"""Esta función Muestra la interfaz de menú"""        
def menu_principal():
    while True:
        print("\n ==== BIENVENIDO AL INVENTARIO ====")
        print("1. Agregar producto.")
        print("2. Mostrar inventario.")
        print("3. Buscar Producto.")
        print("4. Actualizar producto.")
        print("5. Eliminar producto.")
        print("6. Ver estadisticas.")
        print("7. Guardar CSV.")
        print("8. Cargar CSV.")
        print("9. Salir")
        
        while True:
            try:
                opcion = int(input("Seleccione una opción del 1-9:"))
                break
            except ValueError:
                print("Ingrese un Número")
                
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            actualizar_producto()
        elif opcion == 5:
            eliminar_producto()   
        elif opcion == 6:
            calcular_estadisticas()
        elif opcion == 7:
            guardar_csv()
        elif opcion == 8:
            cargar_csv()        
        elif opcion == 9:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, intenta nuevamente.")
            
        
        
    
    
                    
            
    