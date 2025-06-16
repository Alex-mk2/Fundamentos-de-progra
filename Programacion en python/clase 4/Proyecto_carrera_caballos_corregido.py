#importacion de libreria
import random




#Variables globales
pista_validas = [1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400]
pista_disponible = set()



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



#Descripción: Funcion para asignar un bono aleatorio antes de la carrera 
#Dom: caballo
#Rec: bono de velocidad

def asignar_bono(caballo):
    #Se calcula el bono de velocidad entre 0 a 10 km
    bono_velocidad = caballo["velocidad_base"] + random.randint(0,10)
    #Se le asigna el bono dentro del diccionario
    caballo["velocidad_actual"] = bono_velocidad
    return bono_velocidad 

#Descripción: Funcion para que el caballo avanze según su velocidad actual
#Dom: caballo
#Rec: avance de caballo

def avanzar_caballo(caballo):
    #Con esto se sabe cuanto esta recorriendo el caballo...
    mt_por_segundo = (caballo["velocidad_actual"] * 1000)/3600
    avance_caballo = mt_por_segundo
    caballo["posicion"] += avance_caballo
    return avance_caballo


#Descrpción: Funcion que verifica si el caballo se lesiona y actualiza su estado
#Dom: caballo
#Rec:boleano(True si se lesiona, False si no se lesiona)

def verificar_lesion(caballo):
    if lesion_caballo(caballo["probabilidad_lesion"]):
        caballo["disponibilidad_caballo"] = False
        return True
    else:
        return False

#Funcion 6
#Descripción: Funcion para simular la carrera de caballos(Lista dentro de un diccionario)
#Dom: pista, caballos
#Rec: void

def simular_carrera(pista, caballos):
    #Preparar cada caballo
    for caballo in caballos:
        caballo["posicion"] = 0
        caballo["disponibilidad_caballo"] = True
        bono = asignar_bono(caballo)
        print(".", "caballo:", caballo["nombre"], 
              "velocidad final:", caballo["velocidad_actual"], "km/h",
              "(bono:", bono, ")")

#Descripción: Funcion para mostrar los caballos registrados
#Dom: lista_caballos
#Rec:

def mostrar_caballos(lista_caballos):
    for caballo in lista_caballos:
        print(f"Nombre: {caballo['nombre']}, Pista: {caballo['pista']}, Velocidad: {caballo['velocidad_base']} km/h")


#Funcion para generar la asignacion de pista a un caballo
#Dom: void
#Rec: void

def asignar_pista():
    pista = random.choice(pista_validas)
    if(pista not in pista_disponible):
        pista_disponible.add(pista)
        return pista
    else:
        return asignar_pista()


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











#Prueba de funcionalidades...


#Funcion crear caballo (check)
caballo = crear_caballo("Juan", 60, 0.2, 1100)
caballo2 = crear_caballo("Felipe", 55, 0.1, 1000)

#Funcion asignar velocidad caballo (check y corregido)
velocidad = asignar_bono(caballo)


#Validar velocidad (check)
#print(validar_velocidad(velocidad))


#Validar lesion caballo (check)
#print(verificar_lesion(caballo))


#Verificar avance caballo (check)
avance = avanzar_caballo(caballo)
#print(avance)

#Verificar creacion de multiples caballos
caballos = crear_caballos(2)
mostrar_caballos(caballos)


#****************************************Correciones***********************************************#


#-Mostrar_caballos()----------------> sobreescritura...
#-Avance_caballo()------------------> la funcion no llevaba a ningun lado (se hizo correcion general)
#-Similar_carrera()-----------------> no fue probada...
#-Asignar_bono()--------------------> corregido previamente (no entiendo porque se hizo cambio)
#-Menu principal--------------------> borrado, estaba muy desordenado con muchas cosas
#-Legibilidad-----------------------> deben ser ordenados y coherentes, no dejar cosas al lote...
#-Generar funciones-----------------> se genero algunas funciones
#-Variables globales----------------> se configuro pistas validas y que no se repitan
#-Sugerencias-----------------------> orden en el código y modulacion de funciones, si a mi me cuesta leer, imaginense ustedes...
#-Revision: Alex Mellado Gamboa