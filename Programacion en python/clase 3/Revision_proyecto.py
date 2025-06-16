
#Librerias
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



#Descripcion: Funcion que permite crear a un caballo
#Dom: nombre_caballo, velocidad_caballo, probabilidad_lesion
#Rec: diccionario con los datos del caballo a crear

def crear_caballo(nombre_caballo, velocidad_caballo, probabilidad_lesion):
    return{
        "nombre": nombre_caballo,
        "pista": pista,
        "velocidad_base": velocidad_caballo,
        "velocidad_actual": velocidad_caballo,
        "posicion": 0,
        "disponibilidad_caballo": True,
        "probabilidad_lesion": probabilidad_lesion
}
#Se crea un caballo


#Descripcion: Funcion que permite asignar un minimo de velocidad a un caballo
#Dom: caballo (diccionario con elementos del caballo)
#Rec: velocidad_base

def aumento_velocidad_caballo(caballo):

    #Asignacion de velocidad base
    nueva_velocidad = random.randint(0, 10)

    #Se actualiza el diccionario con la nueva velocidad
    caballo["nueva_velocidad"] = caballo["velocidad_base"] + nueva_velocidad

    #Se retorna la nueva velocidad
    return nueva_velocidad


#Descripcion: Funcion que permita asignar una pista a un caballo
#Dom: caballo (diccionario con elementos del caballo)
#Rec: pista asignada al caballo

def asignar_pista(caballo):
    return random.choice(pistas_validas)





#menu principal
# opcion == 1 #mostar cantidad de cab
#opcion == 2 # ingrese la pista
#opcion == 3# #ingrese velocidad
#opcion

#Pistas validas
pistas_validas = [1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400]


#Configuracion del caballo y carrera
nombre = "Caballo1"
velocidad = 60
probabilidad_lesion = 0.1
pista = asignar_pista(pistas_validas)


#Probar aumento velocidad
caballo = crear_caballo(nombre, velocidad, probabilidad_lesion)

#Aumentar velocidad
nueva_velocidad = aumento_velocidad_caballo(caballo)
print("Caballo:", caballo["nombre"], caballo["velocidad_base"], "km/h")


