#Ejercicio 3

#Se crea un diccionario para las evaluaciones
evaluaciones = [ 
    {"cliente": "Sofía", "puntaje": 5, "producto": "Latte"}, 
    {"cliente": "Tomás", "puntaje": 4, "producto": "Tostada Integral"}, 
    {"cliente": "Sofía", "puntaje": 3, "producto": "Latte"}, 
    {"cliente": "Martina", "puntaje": 5, "producto": "Smoothie de Frutilla"}, 
    {"cliente": "Javier",  "puntaje": 4, "producto": "Latte"} 
]

#Decripción: Función para calcular el promedio de puntajes de los clientes
#Dom: Diccionario(evaluaciones)
#Rec: promedio de sastisfaccion(de todos los puntajes)

def promedio_satisfaccion(evaluaciones):
    suma = 0 #Se crea un acumalador para la suma 
    cantidad = 0 #Se va a contar cuantas evalaciones hay
    
    # Recorre cada elemento (diccionario) dentro de la lista 'evaluaciones'
    for evaluacion in evaluaciones:
        #Se va sumar cada puntjae dentro del diccionario
        suma = suma + evaluacion["puntaje"]
        cantidad = cantidad + 1 #Se incrementa el contador de la cantidad de puntaje
    #Promedio = la suma /cantitad total
    promedio = suma / cantidad
    #Devuelve el promedio
    return promedio


# Función que determina el producto con más evaluaciones
# Dom: lista de diccionarios (evaluaciones)
# Rec: string (nombre del producto más evaluado)

def producto_mas_evaluado(evaluaciones):
    productos = []   # Lista para guardar los nombres de productos ya revisados
    max_producto = ""  # Guarda el nombre del producto con más evaluaciones
    max_cantidad = 0  # Guarda la cantidad máxima de evaluaciones encontradas

    # Recorremos cada evaluación en la lista
    for evaluacion in evaluaciones:
        producto_actual = evaluacion["producto"]  # Tomamos el nombre del producto
        # Si el productol actual no esta en la lista de productos(no lo contamos)
        if producto_actual not in productos:  
            productos.append(producto_actual)  # Lo agregamos a la lista de revisados
            cantidad = 0  # Inicializamos un contador para este producto

            # Contamos cuántas veces aparece este producto en todas las evaluaciones
            for evaluacion in evaluaciones:
                #Si el producto coincide
                if evaluacion["producto"] == producto_actual:
                    cantidad = cantidad + 1 #Aumentamos el contador 


            # Si este producto tiene más evaluaciones que el actual máximo, lo actualizamos
            if cantidad > max_cantidad:
                max_cantidad = cantidad # Actualizamos la máxima cantidad de evaluaciones
                max_producto = producto_actual #Actualizamos el producto con más evaluaciones


    return max_producto  # Devolvemos el nombre del producto más evaluado

#Se llama las 2 funciones creadas
#Llamar la funcion con el promedio
promedio = promedio_satisfaccion(evaluaciones)
#Llamar la función con el producto mayor evaluado
producto_mayor = producto_mas_evaluado(evaluaciones)

#Se muestran los resultados
print("Promedio de satisfacción:", promedio)
print("Producto más evaluado:", producto_mayor)