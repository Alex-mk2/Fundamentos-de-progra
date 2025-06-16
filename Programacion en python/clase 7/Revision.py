#Ejercicio de archivo
#Se nos pide crear 3 funciones
#1. Funcion que lea el archivo que contiene  
#2  Función para mostrar los vehiculos con el número por marca
#3. Función para vrear un archivo para que guarde los vehiculos por marca

#Descripción: Función para leer el archivo contenido
#Dom: ruta_archivo
#Rec: lista con el contenido del archivo 

def obtener_datos(ruta_archivo):
    #Se crea una lista para almacenar el contenido
    lista = []
    #Se abre el archivo en modo lectura
    with open(ruta_archivo, "r") as archivo:
        next(archivo) #Omite la cabecera 
        informacion = archivo.read()
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.split(";") #Se separa en coma el contenido
            lista.append(auxiliar)
    return lista


#Descripción: Función para mostrar por el numero de marcas por cada vehiculo 
#Dom: lista_vehiculos
#Rec: lista con la cantidad 
def mostrar_numero_vehiculos_por_marca(lista_vehiculos):
    resultado = [] #Lista vacía donde guardaremos marcas y su conteo
    
    #Recorremos todos los vehiculos en la lista_vehiculos
    for vehiculo in lista_vehiculos:
        marca = vehiculo[0] # Se obtiene la marca del vehículo 
        
        # Recorremos para ver si la marca ya está registrada
        for marca_contada in resultado:
            #Si la marca es igual con la marca registrada
            if marca_contada[0] == marca:
                marca_contada[1] = marca_contada[1] + 1 #Se aumenta la marca registrada 
    
        else:
            resultado.append([marca, 1]) #Se agrega un nuevo registro
    
    return resultado 


#Descripción: Función que guarda los vehículos por marca en un archivo
#Dom: ruta_archivo x mostrar_numero_vehiculos_por_marca
#Rec: archivo de texto creado con los datos

def guardar_vehiculos_por_marca(ruta_archivo, lista_vehiculos):
    #Se abre el archivo nuevo en modo escritura
    with open(ruta_archivo, "w") as resultado:
        resultado.write("Marca; Cantidad \n" + str(marcas))
        print("Se ha escrito el resultado correctamente\n")









#Procesamiento de datos

#Se llama la función para leer el archivo
lectura = obtener_datos("vehículos.csv")
print("Lectura completa:", lectura) 

#Se llama la funcion para las marcas de vehículos 
marcas = mostrar_numero_vehiculos_por_marca(lectura)
print("Cantidad de vehículos por marca:", marcas)
#Se escribe el archivo nuevo
escribir_archivo = guardar_vehiculos_por_marca("vehiculos_por_marca.csv", marcas)

