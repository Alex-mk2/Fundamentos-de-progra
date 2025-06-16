#Descripcion del problema entre conjuntos
#Si consideramos dos conjuntos de enteros positivos A = [a0, a1, . . . , an−1]
#y B = [b0, b1, . . . , bn−1]. Se dice que un numero
#entero positivo x existe ’entre los conjuntos’ si:

#-* Todos los elementos de A son divisores exactos de x
#-* Todos los elementos de B son divisibles por x

#Es decir, todo numero divisible por cada elemento A y divisor de cada elemento de B, es un numero que existe 
#’Entre Conjuntos’. Por ejemplo:
#Primer caso
#Si A = [4, 2] y B = [16, 96, 32], los n´umeros que cumplen ambas condiciones son 4, 8 y 16, 
#por lo tanto, los numeros que existen ’entre conjuntos’ son 4, 8 y 16


#Segundo caso
#Si A = [3, 5] y B = [15, 30, 12], no existe un numero que cumpla ambas condiciones, 
#por lo tanto, no hay x que satisfaga dicha propiedad
#Se requiere que construya un programa en Python que dados los conjuntos A y B, 
#entregados como listas, indique el conjunto de n´umeros que cumplen con la propiedad de 
#existir ’Entre Conjuntos’.



#Librerias: Se utilizara math
from math import gcd


#Descripcion: Funcion que permite determinar el minimo comun multiplo entre dos numeros
#Dom: lista A X lista B
#Rec: numero

def mcm (listaA, listaB):
    return abs(listaA * listaB) // gcd(listaA, listaB)


#Descripcion: Funcion que permite calcular el minimo comun entre una lista de numeros
#Dom: listaA
#Rec: numero

def mcm_lista(listaA):
    i = 1
    resultado = listaA[0]
    while(i < len(listaA)):
        resultado = mcm(resultado, listaA[i])
        i = i + 1
    return resultado


#Descripcion: Funcion que permite determina el maximo comun divisor entre dos numeros
#Dom: listaA X listaB
#Rec: numero

def mcd_lista(listaA):
    i = 1
    resultado = listaA[0]
    while(i < len(listaA)):
        resultado = gcd(resultado, listaA[i])
        i = i + 1
    return resultado


#Descripcion: Funcion que permite determinar si existe un numero entre dos conjuntos
#Dom: listaA X listaB
#Rec: lista de numeros entre conjuntos

def entre_conjuntos(listaA, listaB):
    resultado = []

    #Se obtiene el minimo comun entre los elementos de A 
    mcmA = mcm_lista(listaA)
    #Se obtiene el maximo comun entre los elementos de B
    mcdB = mcd_lista(listaB)

    
    x = mcmA

    #Se busca entre los conjuntos A y B
    while(x <= mcdB):
        if(mcdB % x == 0):
            resultado.append(x)
        x = x + mcmA
    return resultado


print(entre_conjuntos([4, 2], [16, 96, 32]))
print(entre_conjuntos([3, 5], [15, 30, 12]))



