#Funcion para asignar un bono aleatorio antes de la carrera 

import random


def asignar_bono(caballo):
    #Se calcula el bono de velocidad entre 0 a 10 km
    bono_velocidad = random.randint(0,10)
    #Se le asigna el bono dentro del diccionario
    caballo["velocidad_base"] = caballo["velocidad_base"] + bono_velocidad
    return bono_velocidad

#funcion para que el caballo avanze según su velocidad actual
def avanzar_caballo(caballo):
    avance = caballo["velocidad_actual"]
    caballo["posicion"] = caballo["posicion"] + avance
    return avance

#funcion que verifica si el caballo se lesiona
#def verificar_lesion(caballo):
    #if(lesion_caballo(caballo["probabilidad_lesion"]))
         #caballo["dispomibilidad_caballo"] = False
         #return True)

#Funcion 6
#Descripción: Funcion para simular la carrera
#Dom: pista, caballos
#Rec:
#Antes que empieze la carrera se le agrega un bono de velocidad aleatoria
#def simular_carrera(pista, caballos):
    #Preparar cada caballo
    #for caballo in caballos:
        #caballo["posicion"] = 0
        #caballo["disponibilidad_caballo"] = True
        #bono = asignar_bono_velocidad(caballo)
        #print(".", "caballo:", caballo["nombre"], 
              #"velocidad final:", caballo["velocidad_actual"], "km/h",
              #"(bono:", bono, ")")
        



#Prueba bono velocidad


#crear caballos
caballos = [
    {"nombre": "Caballo 1", "velocidad_base": 20, "probabilidad_lesion": 0.1},
    {"nombre": "Caballo 2", "velocidad_base": 25, "probabilidad_lesion": 0.2},
    {"nombre": "Caballo 3", "velocidad_base": 30, "probabilidad_lesion": 0.15}
]

asignar_bono(caballos[0])
print("Caballo 1 - Velocidad base:", caballos[0]["velocidad_base"], "km/h")