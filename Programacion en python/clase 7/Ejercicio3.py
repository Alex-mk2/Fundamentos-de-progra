#Lectura de archivos 
#Restricciones: No se puede utilizar csv ni pandas



#Descripcion: Funcion que permite la lectura del archivo
#Dom: Archivo
#Rec: lista con el contenido del archivo (matriz de listas de listas)

def leerArchivo(archivo):
    lista = []
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos:
        next(datos) #Omitir el encabezado
        informacion = datos.read()
        informacion = informacion.splitlines() #Sublista por cada linea
        for dato in informacion:
            auxiliar = dato.split(";") #Separar por cada ";" separar posiciones
            #Se eliminan las comillas de cada elemento del archivo
            auxiliar = [elemento.strip('"') for elemento in auxiliar] #Eliminar comillas y espacios
            auxiliar[0] = int(auxiliar[0]) #Primera posicion entero
            auxiliar[1] = int(auxiliar[1]) #Segunda posicion entero
            auxiliar[4] = float(auxiliar[4]) if auxiliar[4] != "ND" else None
            auxiliar[7] = float(auxiliar[7])
            auxiliar[8] = float(auxiliar[8])
            auxiliar[9] = float(auxiliar[9])
            auxiliar[10] = float(auxiliar[10])
            auxiliar[11] = float(auxiliar[11])
            lista.append(auxiliar)
        #Se cierra el archivo    
        datos.close()
    return lista



#Descripcion: Funcion que permite contabilizar la cantidad de titulos por categoria
#Dom: archivo procesado como lista
#Rec: diccionario con los elementos por genero de juego


#Es contar elementos (lista = archivo procesado y limpiado)
def contar_titulos_por_genero(lista):
    contador = {} #Diccionario vacio (--------> contador = 0)-------> porque estamos accediendo
    #--------------------------------------------------------> a una posicion especifica del archivo
    for fila in lista:
        categoria = fila[5] #Se toma el genero del juego "Genero"
        if(categoria not in contador):
            contador[categoria] = 1 #Solo toma el valor 1 si no esta en la categoria
        else: #Si existe en la categoria "genero"
            contador[categoria] += 1
    return contador



#Descripcion: Funcion que permite calcular ventas totales por genero
#Dom: Lista procesada del archivo
#Rec: diccionario con las ventas totales por genero

def calcular_ventas_por_genero(lista):
    ventas = {} #diccionario vacio
    for fila in lista:
        categoria = fila[5] #Tomando el genero del juego
        if(categoria not in ventas):
            ventas[categoria] = fila[11]
        else:
            ventas[categoria] += fila[11]
    return ventas



#Ejecucion principal

#Primera funcion
lectura = leerArchivo("video_games_sales.csv")


#Segunda funcion
categoria = contar_titulos_por_genero(lectura)
print("Cantidad de titulos por categoria: ", categoria)


#Tercera funcion
ventas = calcular_ventas_por_genero(lectura)
print("Ventas globales por genero: ", ventas)