import random 


#Descripcion: Funcion que simula la lesion de un caballo
#Dom: probabilidad_lesion
#Rec: booleano (True o False)

def lesion_caballo(probabilidad_lesion):
    if(0.05 <= probabilidad_lesion <= 0.3):
        return random.random() < probabilidad_lesion
    else:
        print("probabilidad de lesion no valida")
        return None
    


#Descripcion: Funcion para validar la pista 
#Dom: distancia_pista
#Rec: booleano (True o False)

def validar_pista(distancia_pista):
    opciones_validas = [1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400]
    if(distancia_pista not in opciones_validas):
        return False
    else:
        return True


#Descripcion: Funcion para validar el numero de caballos
#Dom: num_caballos
#Rec: booleano (True o False)

def validar_caballos(num_caballos):
    if(2 <= num_caballos <= 16):
        return True
    else:
        return False

#Descripcion: Funcion que valida el rango de velocidad de un caballo
#Dom: velocidad_caballo
#Rec: booleano (True o False)

def validar_velocidad(velocidad_caballo):
    if(50 <= velocidad_caballo <= 65):
        return True
    else:
        return False

#Menu principal
lesion = float(input("Ingrese la probabilidad de lesion del caballo (0.05 - 0.3): "))
pista = int(input("Ingrese la distancia de la pista (1000, 1100, 1200, 1300, 1600, 1700, 1800, 2000, 2400): "))
num_caballos = int(input("Ingrese el numero de caballos (2 - 16): "))
velocidad = float(input("Ingrese la velocidad del caballo (50 - 65): "))

#Verificaciones lesion caballo
resultado = lesion_caballo(lesion)
if resultado == True:
    print("El caballo se ha lesionado")
elif resultado == False:
    print("El caballo no se ha lesionado")


#Verificaciones pista
if(validar_pista(pista) == True):
    print("La pista es valida")
else:
    print("La pista no es valida")


#Verificaciones del numero de caballos
if(validar_caballos(num_caballos) == True):
    print("El numero de caballos es valido")
else:   
    print("El numero de caballos no es valido")


#Verificaciones de la velocidad del caballo
if(validar_velocidad(velocidad) == True):
    print("La velocidad del caballo es valida")
else:
    print("La velocidad del caballo no es valida")