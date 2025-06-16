#importacion de libreria
import random
import time

# ======================= VARIABLES GLOBALES ================================
pistas_validas = [1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400]
carriles_ocupados = set()  # Carriles ya asignados
caballos = [] # Lista de caballos
#Set = Crea un conjunto vacío que almacena valores únicos(no dúplicados) 



#Función 1
#Descripcion: Funcion que simula la lesion de un caballo
#Dom: probabilidad_lesion
#Rec: booleano (True o False)

def lesion_caballo(probabilidad_lesion):
    if(0.05 <= probabilidad_lesion <= 0.3): #30 y 5%
        return random.random() < probabilidad_lesion #Devuelve al alzar una probalidad dentro de ese rango valido
    else:
        print("probabilidad de lesion no valida")
        return None
    
#Función 2
#Descripcion: Funcion para validar la pista 
#Dom: distancia_pista
#Rec: booleano (True o False)

def validar_pista(distancia_pista):
    pistas_validas = [1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400]
    if(distancia_pista not in pistas_validas):
        return False
    else:
        return True

#Función 3
#Descripcion: Funcion para validar el numero de caballos
#Dom: num_caballos
#Rec: booleano (True o False)

def validar_caballos(num_caballos):
    if(2 <= num_caballos <= 16):
        return True
    else:
        return False

#Funcion 4

#Descripcion: Funcion que valida el rango de velocidad de un caballo
#Dom: velocidad_caballo
#Rec: booleano (True o False)

def validar_velocidad(velocidad_caballo):
    if(50 <= velocidad_caballo <= 65):
        return True
    else:
     return False

#Funcion 5

#Descripcion: Funcion que permite crear a un caballo
#Dom: nombre_caballo, velocidad_caballo, probabilidad_lesion
#Rec: diccionario con los datos del caballo a crear

def crear_caballo(nombre_caballo, velocidad_caballo, probabilidad_lesion, carril):
    return {
        "nombre": nombre_caballo,
        "carril": carril,  # Este es el número de carril asignado 
        "velocidad_base": velocidad_caballo,
        "velocidad_actual": velocidad_caballo,  # Se actualiza en carrera
        "posicion": 0,  # Parte desde cero
        "disponibilidad_caballo": True,  # Está disponible mientras no se lesione
        "probabilidad_lesion": probabilidad_lesion
    } 
#Se crea un caballo para la carrera"


#Funcion 6

#Descripción: Funcion para asignar un bono aleatorio antes de la carrera 
#Dom: caballo
#Rec: bono de velocidad

def asignar_bono(caballo):
    #Se calcula el bono de velocidad entre 0 a 10 km
    bono_velocidad = random.randint(0,10)
    #Se le asigna el bono dentro del diccionario
    caballo["velocidad_actual"] = caballo["velocidad_base"] + bono_velocidad
    return bono_velocidad #Devuelve el bono aleatorio


#Funcion 7

#Descripción: Funcion para que el caballo avanze según su velocidad actual
#Dom: caballo
#Rec: avance de caballo

def avanzar_caballo(caballo):
    #Con esto se sabe cuanto esta recorriendo el caballo...
    mt_por_segundo = (caballo["velocidad_actual"] * 1000)/3600 # Convierte km/h a m/s: km/h * (1000 m / 1 km) * (1 h / 3600 s)
    avance_caballo = mt_por_segundo
    caballo["posicion"] = caballo["posicion"] + avance_caballo
    return avance_caballo

#Funcion 8

#Descripción: Funcion para mostrar los caballos registrados
#Dom: lista_caballos
#Rec: void (no retorna nada)

def mostrar_caballos(lista_caballos):
    for caballo in lista_caballos:
        print(f"Nombre: {caballo['nombre']}, carril: {caballo['carril']}, Velocidad: {caballo['velocidad_base']} km/h")


#Funcion 9

#Funcion para generar la asignacion de carril válido
#Dom: void
#Rec: carril

#Nota: Función no tiene parametros ya que se usa set
def asignar_carril():
    #Lista para almacenar los carriles disponibles
    carriles_disponibles = []
    # Generar carriles disponibles del 1 al 16 que no estén ocupados
    for carril in range(1, 17):
        if carril not in carriles_ocupados:
            carriles_disponibles.append(carril)

    # Validar si hay carriles disponibles
    if not carriles_disponibles:
        print("No hay carriles disponibles. Todos los carriles están ocupados.")
        return None # Si la lista de disponibles está vacía
    
    # Mostrar carriles disponibles
    print("Carriles disponibles:", carriles_disponibles)
        
    # Bucle hasta que se ingrese un carril válido
    while True:
        carril = int(input("Ingrese número de carril (1 al 16): "))
        
        if carril not in carriles_disponibles:
            print("Carril inválido o ya ocupado. Intente de nuevo.")
        else:
            carriles_ocupados.add(carril)
            print("Carril asignado:", carril)
            return carril


#Función 10

#Funcion para crear multiples caballos
#Dom: num_caballos
#Rec: caballos

def crear_caballos(num_caballos):
    caballos = []
    #Se utiliza la funcion de verificar cantidad
    if not validar_caballos(num_caballos):
        print("Se debe ingresar al menos dos caballos...")
    
    #Ahora para crear más
    for i in range(num_caballos):
        print(f"\n--- Configurando Caballo {i+1} ---") 
        
        #Se le pide al usuario que ingrese el nombre del caballo
        nombre_caballo = input("Ingrese nombre del caballo: ") 
        
        # Solicitar y validar velocidad del caballo
        velocidad = 0 # Inicializa la velocidad
        
        # Se crea un Bucle infinito hasta que la velocidad sea válida
        while True: 
            #Se le pide al usuario que elija la velocidad del caballo
            velocidad = int(input("Ingrese la velocidad del caballo (50 - 65): ")) 
            #Si la velocidad es válida dentro del rango se sale del ciclo 
            if validar_velocidad(velocidad):
                break 
            else:
                print("Velocidad no válida. Debe estar entre 50 y 65 km/h. Ingrese de nuevo.")

        # Solicitar y validar probabilidad de lesión
        probabilidad_lesion = 0.0 # Inicializar la probbilidad de lesión

        # Bucle infinito hasta que la probabilidad de lesión sea válida
        while True: 
            #Se le pide al usuario que ingrese la probabilidad de lesión
            probabilidad_lesion = float(input("Ingrese la probabilidad de lesión (0.05 - 0.3): "))
            
            # Si la probabilidad es válida, salimos de este bucle
            if 0.05 <= probabilidad_lesion <= 0.3:
                break 
            else:
                print("Probabilidad inválida. Debe estar entre 0.05 y 0.3. Ingrese de nuevo.")
        
        carril = asignar_carril()
        caballo = crear_caballo(nombre_caballo, velocidad, probabilidad_lesion, carril)
        caballos.append(caballo)

    return caballos

# AQUI EMPIEZA LA SIMULACION DE CARRERA

#Funcion 11
#Descripción: Función para determinar el caballo ganador
#Dom: callos x pista
#Rec: caballo que llego primero a la meta es el ganador

def caballo_ganador(caballos, pista):
    for caballo in caballos:
        if caballo["posicion"] >= pista:
            return caballo  # Devuelve el primero que llegue




#Funcion 12

#Descripción: Función para iniciar la carrera 
#Dom: caballos
#rec: void

def comenzar_carrera(caballos, pista):
    # Todos los caballos comienzan desde 0 metros y están disponibles
    for caballo in caballos:
        caballo["posicion"] = 0
        caballo["disponibilidad_caballo"] = True
        asignar_bono(caballo)
    
    #Inicializar las variables
    carrera_termina = False # Se inicializa en un falso para saber cuando termina la carrera en el bucle
    print("\n¡Comienza la carrera!")
    print("-" * 60)

    while not carrera_termina:
        time.sleep(1)  # Espera 1 segundo para iniciar la carrera
        print("\nActualización de posiciones:")
        #Se recorre cada caballos en la lista de caballos
        for caballo in caballos:
            if caballo["disponibilidad_caballo"]:
                # Ver si se lesiona en el transcuro de la carrera(función de lesion de caballo)
                    if lesion_caballo(caballo["probabilidad_lesion"]):
                        caballo["disponibilidad_caballo"] = False
                        print(caballo["nombre"], "se lesionó.")
                    else:
                        avance = avanzar_caballo(caballo) #Si no se lesionó, avanza en la pista
                        print(f"{caballo['nombre']} avanzó {round(avance, 2)} m (Total: {round(caballo['posicion'], 2)} m)")

        ganador = caballo_ganador(caballos, pista) #Se llama la función para determinar cual fue el caballo ganador
        
        #Verificar el ganador
        if ganador:
            print(f"\n ¡{ganador['nombre']} ha ganado la carrera!")
            carrera_termina = True #Se termina la carrera

        print("-" * 60)

# Verificar si todos los caballos están lesionados
        todos_lesionados = True
        for caballo in caballos:
            if caballo["disponibilidad_caballo"]:
                todos_lesionados = False
        
        if todos_lesionados:
            print("\nTodos los caballos se lesionaron. La carrera termina sin ganador.")
            carrera_termina = True


#Función 13

#Funcion que permite mostrar las posiciones de los caballos
#Dom: caballos
#Rec: void

def mostrar_posiciones(caballos):
    print("*************Posiciones*********************")
    for caballo in caballos:
        if(caballo["disponibilidad_caballo"]):
            print(f"{caballo['nombre']} está en la pista {caballo['carril']} a {round(caballo['posicion'], 2)} m")
        else:
            print(f"{caballo['nombre']} se ha lesionado y no puede continuar.")
    
    



#=============== MENÚ PRINCIPAL ===============
opcion = 0
pista = 0
while opcion != 6:
    print("\n--- MENÚ CARRERA DE CABALLOS ---")
    print("1) Configurar pista")
    print("2) Agregar caballo")
    print("3) Mostrar caballos")
    print("4) Iniciar carrera")
    print("5) Resultados de la carrera")
    print("6) Salir")
    #Se le preguntara al usuario que elija una opción
    opcion = int(input("Elige una opción (1-6): "))
    
    # Opción 1: Configurar pista
    if opcion == 1:
        print("Pistas válidas disponibles:", pistas_validas) #Se va mostrar las pistas validas
        distancia = int(input("Ingrese la distancia de la pista: "))
        if validar_pista(distancia):
            pista = distancia
            print("Pista configurada a", pista, "metros")
        else:
            print("Distancia no válida. Debes elegir una de las opciones mostradas.")


    # Opción 2: Agregar caballos
    elif opcion == 2:
        num = int(input("Número de caballos (2-16): "))
        if validar_caballos(num): #Se llama la funcion de validar caballos(2 - 16)
            caballos = crear_caballos(num) #Se llama la función ya que se le pregunta prob lesion, nombre, etc.
        else:
            print("Número de caballos inválido: Debe registrar al menos dos caballos")

    # Opción 3: Mostrar caballos
    elif opcion == 3:
        if(not caballos):
            print("No hay caballos registrados")
        else:
            print("Caballos registrados:")
            mostrar_caballos(caballos)
            mostrar_posiciones(caballos)

    # Opción 4: Iniciar carrera
    elif opcion == 4:
        if(not caballos):
            print("No hay caballos registrados")
        else:
            comenzar_carrera(caballos, pista)
    
    # Opción 5: Resultados de la carrera
    elif opcion == 5:
        if not caballos:
            print("No hay caballos registrados")
        else:
            print("Resultados de la carrera:")
            mostrar_posiciones(caballos)

    # Opción 6: Salir
    elif opcion == 6:
        print("Salir")


    # Opción inválida
    else:
        print("Opción inválida: Debe elegir un número del 1 al 6")
