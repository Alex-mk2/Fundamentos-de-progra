


#Matriz-----> contiene elementos del tipo (i, j)
#Matriz-----> [0][0] [0][1] [0][2]
#             [1][0] [1][1] [1][2]
#             [2][0] [2][1] [2][2]


#------> matriz ------------->[2] [3] ------------> transpuesta A 
#                                                   [2] [5] [7]
#                             [5] [8]               [3] [8] [9]
#                             [7] [9]




#Descripcion: Funcion que permite procesar una matriz a matriz transpuesta
#Dom: matriz (lista de listas)
#Rec: lista con el contenido de la matriz (transpuesto)

#Cambio de posiciones de cada elemento de la matriz



def transponer_matriz(matriz):
    lista_transpuesta = []
    #Elemento i de la matriz (filas)
    for i in range(len(matriz[0])): #For externo para recorrer las filas
        lista_transpuesta.append([])
        #Elemento j de la matriz (columnas)
        for j in range(len(matriz)): #For interno para recorrer columnas
            lista_transpuesta[i].append(matriz[j][i]) #Operando tanto con la fila y columna de la matriz
    return lista_transpuesta


#-------> matriz vertical-----------> [1] [7] --------------> [1]----------> [0][0]
#                                     [2] [5] --------------> [2]----------> [1][0]
#                                     [3] [4] --------------> [3]----------> [2][0]
#                                             --------------> [7]----------> [0][1]
#------->(3 x 2)------> 3 filas y 2 columnas



# (3 x 3)
#-------------------------------> [1] [4] [7] ---------------> [1] -------> [0][0]
#                                 [2] [9] [1]                  [4]--------> [1][1]
#                                 [3] [7] [2]                  [7]--------> [2][2]





#Ejecucion principal del programa
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpuesta = transponer_matriz(matriz)
print("matriz original:", matriz)

print("matriz transpuesta: ", transpuesta)



