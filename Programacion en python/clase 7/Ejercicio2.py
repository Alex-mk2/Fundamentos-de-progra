#Sectores representados por una matriz



#Descripcion: Funcion que permite procesar los sectores como matriz
#Dom: void
#Rec: matriz

def procesar_sectores():
    filas = ['A', 'B', 'C', 'D'] #Filas de la matriz
    columnas = ['1', '2', '3', '4'] #Columnas de la matriz
    matriz = [f + c for f in filas for c in columnas] #-------> f + c (suma de strings)--------> concatenan
    return matriz

#For f in filas:
#  for c in columnas:
#----------------> ultimo valor (D4).....


#--------> f + c por cada f en filas, por cada c en columnas
#--------> "cada elemento de la combinacion de filas y columnas"
#--------> "A1","B1","C1","D1"
#--------> "A2","B2","C2","D2"
#--------> "A3","B3","C3","D3"
#--------> "A4","B4","C4","D4"



#Descripcion: Funcion que permite procesar las rutas de los drones
#Dom: matriz
#Rec: Rutas de los drones

def rutas_no_visitadas_drones(matriz):
    ruta_a = ['A1', 'A2', 'A3', 'B3', 'B2', 'B1'] #Ruta del dron A
    ruta_b = ['D4', 'C4', 'B4', 'B3', 'C3', 'D3'] #Ruta del dron B
    ruta_c = ['D1', 'D2', 'D3', 'C3', 'C2', 'D2'] #Ruta del dron C

    #Se debe procesar como teoria de conjuntos (rutas de drones)
    setA = set(ruta_a) #Elementos asignados, pero tambien unicos (no repetidos)
    setB = set(ruta_b)
    setC = set(ruta_c)

    #Ahora se une estos conjuntos (operador de union)
    rutas_unidas = setA | setB | setC #A union B union C

    #Otra forma de unir los conjuntos
    rutas_unidas = setA.union(setB).union(setC)

    #Ahora los que no fueron visitados-------> (diagrama de venn (matriz) - rutas unidas (no tienen repeticion))
    no_visitados = set(matriz) - rutas_unidas
    return list(no_visitados)


#Descripcion: Funcion que permite determinar sectores solapados (que han sido 
#visitados mas de una vez)
#Dom: matriz
#Rec: lista con los sectores solapados

def sectores_solapados(matriz):
    ruta_a = ['A1', 'A2', 'A3', 'B3', 'B2', 'B1'] #Ruta del dron A, B, C
    ruta_b = ['D4', 'C4', 'B4', 'B3', 'C3', 'D3']
    ruta_c = ['D1', 'D2', 'D3', 'C3', 'C2', 'D2']

    #Se debe procesar como teoria de conjuntos (rutas de drones)
    setA = set(ruta_a)
    setB = set(ruta_b)
    setC = set(ruta_c)

    #Ahora se une estos conjuntos (operador de union)
    rutas_unidas = setA | setB | setC

    #Ahora se intercepta para encontrar los sectores solapados #Intersección de conjuntos
    solapados = rutas_unidas & set(matriz)

    #Otra forma
    #solapados = rutas_unidas.intersection(set(matriz))
    return list(solapados)


#Descripcion: Funcion que permite conocer la eficiencia de cobertura de los drones
#Dom: matriz
#Rec: lista con los sectores unicos visitados por los drones y porcentaje

def eficiencia_cobertura_drones(matriz):
    ruta_a = ['A1', 'A2', 'A3', 'B3', 'B2', 'B1']
    ruta_b = ['D4', 'C4', 'B4', 'B3', 'C3', 'D3']
    ruta_c = ['D1', 'D2', 'D3', 'C3', 'C2', 'D2']

    #Se debe procesar como teoria de conjuntos (rutas de drones)
    setA = set(ruta_a)
    setB = set(ruta_b)
    setC = set(ruta_c)

    #Ahora se une estos conjuntos (operador de union)
    rutas_unidas = setA | setB | setC

    total_sectores = len(matriz)
    sectores_visitados = len(rutas_unidas)

    #Se obtiene la cobertura
    cobertura = (sectores_visitados / total_sectores) * 100 #porcentaje de cobertura

    return list(rutas_unidas), cobertura



#Ejecucion
sectores = procesar_sectores()


#Rutas que no han sido visitadas por los drones
rutas_no_visitadas = rutas_no_visitadas_drones(sectores)
print("Sectores que no han sido visitados por los drones: ", rutas_no_visitadas)


#Rutas que han sido visitadas mas de una vez
solapados = sectores_solapados(sectores)
print("Sectores que han sido visitados mas de una vez: ", solapados)


#Eficiencia de la cobertura de los drones
sectores_visitados, cobertura = eficiencia_cobertura_drones(sectores)
print("Porcentaje de cobertura de los drones:", cobertura)
print("Sectores visitados por los drones: ", sectores_visitados)