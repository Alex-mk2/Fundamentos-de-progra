#importacion de libreria
import random


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
    opciones_validas = [1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400]
    if(distancia_pista not in opciones_validas):
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
        "pista": carril,  # Este es el número de carril asignado automáticamente
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
    mt_por_segundo = (caballo["velocidad_actual"] * 1000)/3600
    avance_caballo = mt_por_segundo
    caballo["posicion"] = caballo["posicion"] + avance_caballo
    return avance_caballo

#Funcion 8

#Descripción: Funcion para mostrar los caballos registrados
#Dom: lista_caballos
#Rec: void (no retorna nada)

def mostrar_caballos(lista_caballos):
    for caballo in lista_caballos:
        print(f"Nombre: {caballo['nombre']}, Pista: {caballo['pista']}, Velocidad: {caballo['velocidad_base']} km/h")



#Funcion 9
#Funcion para generar la asignacion de pista a un caballo
#Dom: void
#Rec: void

#Variables globales
pista_validas = [1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400]
pista_disponible = set() #set: va tomar lps valor unicos(no duplicados en la pista)
 

def asignar_pista():
    pista = random.choice(pista_validas)
    if(pista not in pista_disponible):
        pista_disponible.add(pista)
        return pista
    else:
        return asignar_pista()



#Funcion 10

#Funcion para crear multiples caballos
#Dom: caballos
#Rec: caballos

def crear_caballos(num_caballos):
    caballos = []

    #Se utiliza la funcion de verificar cantidad
    if not validar_caballos(num_caballos):
        print("Se debe ingresar al menos dos caballos...")
    

    #Ahora para crear más
    for i in range(num_caballos):
        nombre_caballo = input("Ingrese nombre del caballo: ")
        velocidad = int(input("Ingrese la velocidad del caballo: "))
        probabilidad_lesion = float(input("Ingrese la probabilidad de lesion: "))

        #Ahora que se incorporo la creacion de multiples caballos
        pista = asignar_pista()
        caballo = crear_caballo(nombre_caballo, velocidad, probabilidad_lesion, pista)
        caballos.append(caballo)
    
    return caballos


def caballo_ganador(caballos, pista):
    for caballo in caballos:
        if caballo["posicion"] >= pista:
            return caballo

#Función para iniciar la carrera 
#Dom: caballos
#rec:
def comenzar_carrera(caballos):
    for caballo in caballos:
        asignar_bono 

# Lista donde se guardarán los caballos creados
caballos = []
pista = 0  # se inicializa en 0 pq no esta definida

opcion = 0
while opcion != 5:
    print("\n--- MENÚ CARRERA DE CABALLOS ---")
    print("1) Configurar pista")
    print("2) Agregar caballo")
    print("3) Mostrar caballos")
    print("4) Iniciar carrera")
    print("5) Salir")
    opcion = int(input("Elige una opción (1-5): "))

    # Opción 1: Configurar pista
    if opcion == 1:
        distancia = int(input("Distancia de la pista (metros): "))
        if validar_pista(distancia):
            pista = distancia
            print("Pista configurada a", pista, "metros!")
        else:
            print("Distancia no válida")

    # Opción 2: Agregar caballos
    elif opcion == 2:
        num = int(input("Número de caballos (2-16): "))
        if validar_caballos(num):
            caballos = crear_caballos(num)
        else:
            print("Número de caballos inválido")

    # Opción 3: Mostrar caballos
    elif opcion == 3:
        mostrar_caballos(caballos)

    # Opción 4: Iniciar carrera (completa esto después)
    elif opcion == 4:
        print("Iniciando carrera...")

    # Opción 5: Salir
    elif opcion == 5:
        print("Salir")
    