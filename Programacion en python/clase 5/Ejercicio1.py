#Sistema de reservas de salas

#Una universidad desea implementar un sistema que permita la reserva 
#De salas de estudio para los estudiantes en un horario determinado
#Para eso se le entregará la fecha, nombre y hora


#Para eso se le pide la creacion de las siguientes funciones
#-1: Una funcion que permita agregar una reserva
#-2: Funcion que permita mostrar las reservas
#-3: Funcion que permita cancelar una reserva
#-4: Funcion que permita mostrar reservas por fecha



#Se entrega el diccionario a dicha reserva
#Es un diccionario de dos niveles (fecha (primer nivel)- informacion(segundo nivel))
reservas = {
    "2025-05-22": [
        {"nombre_estudiante": "Camila", "hora": "10:00"}, #Esto son las keys (y esto es lo que se recorrre)
        {"nombre_estudiante": "Ignacio", "hora": "12:00"}
    ],
    "2025-05-23": [
        {"nombre_estudiante": "Valeria", "hora": "09:30"}
    ]
}

#En particular: ¿Que diferencias se puede apreciar respecto a otras estructuras de diccionario?




#Descripcion: funcion que permite agregar una reserva sin repeticiones
#Dom: reserva X fecha X nombre X hora
#Rec: nueva reserva creada

def agregar_reserva(reservas, fecha, nombre, hora):
    nueva_reserva = {"nombre_estudiante": nombre, "hora": hora}

    #Ahora se comprueba si no hay reservas
    if(fecha not in reservas):
        reservas[fecha] = []
    

    #Ahora se quiere buscar si existe una fecha 
    for reserva in reservas[fecha]:
        if(reserva["nombre_estudiante"] == nombre and reserva["hora"] == hora):
            print("Ya existe la reserva")
            return False
    
    #En el caso que no exista, se agrega
    reservas[fecha].append(nueva_reserva)
    return True



#Descripcion: Funcion que muestra las reservas realizadas
#Dom: reserva
#Rec: mostrar por pantalla todas las reservas 

def mostrar_reservas(reservas):
    for fecha in reservas.keys():
        print(f"Fecha: {fecha}")
        for reserva in reservas[fecha]:
            print(f" - {reserva['hora']} → {reserva['nombre_estudiante']}")



#--------->fecha------>reservas.keys()---------->"fechas"--------> reserva--------> (nombres, hora)


#Descripcion: Funcion que permite cancelar una reserva
#Dom: reservas X fecha X nombre
#Rec: reserva cancelada

def cancelar_reserva(reservas, fecha, nombre):
    
    #Si no hay fecha en reservas
    if(fecha not in reservas):
        print("No hay reservas por esa fecha")
    
    #Buscamos todas las reservas por fecha...
    for i, reserva in enumerate(reservas[fecha]):
        #Si encontramos el nombre
        if(reserva["nombre_estudiante"] == nombre):
            #Se elimina reserva asociada a esa fecha
            del reservas[fecha][i] #Se asemeja a una matriz (i, j)
            print("Reserva cancelada")
    


#Descripcion: Funcion que permite mostrar las reservas por fecha
#Dom: reservas X fecha
#Rec: reservas asociadas a esa fecha

def mostrar_reserva_por_fecha(reservas, fecha):
    if(fecha in reservas and reservas[fecha]):
        print(f"Reservas asociadas a la fecha: {fecha}")
        for reserva in reservas[fecha]:
            print(f" - {reserva['hora']} → {reserva['nombre_estudiante']}")
    else:
        print("No hay reservas asociadas a esa fecha")


#Menu principal para el usuario
#Menu de opciones para el usuario
opcion = 0
while (opcion != 4):
    print("****-Sistema de reservas-****")
    print("0. Imprimir las reservas")
    print("1. Agregar reserva")
    print("2. Cancelar reserva")
    print("3. Buscar reservas por fecha")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if(opcion == 0):
        print("Las reservas son:")
        mostrar_reservas(reservas)
    
    elif(opcion == 1):
        fecha = input("Ingrese una fecha en formato (YYYY-MM-DD): ")
        nombre = input("Ingrese el nombre del estudiante: ")
        hora = input("Ingrese la hora en formato (00:00): ")
        reserva = agregar_reserva(reservas, fecha, nombre, hora)
        if(reserva):
            print("Reserva creada con exito")
        else:
            print("La reserva ya existe")
    

    elif(opcion == 2):
        nombre = input("Ingrese el nombre del estudiante: ")
        fecha = input("Ingrese una fecha en formato (YYYY-MM-DD): ")
        reserva = cancelar_reserva(reservas, fecha, nombre)
        
        
    elif(opcion == 3):
        fecha = input("Ingrese una fecha en formato (YYYY-MM-DD): ")
        reserva = mostrar_reserva_por_fecha(reservas, fecha)
    
    
    elif(opcion == 4):
        print("Termino ejecucion...")



