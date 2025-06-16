#En los sistemas de autocorrección de texto, 
#como los utilizados en los teléfonos móviles, es necesario determinar
#cuál es la palabra más cercana a lo que el usuario escribió por error. 
#Una forma sencilla de medir esa cercanía es mediante la distancia de Hamming.


#*-La distancia Hamming entre 101101001 y 101001111 es 3, pues hay 3 caracteres que difieren.
#*-La distancia Hamming entre tener y Tener es 1, pues hay 1 caracter que difiere.
#*-La distancia Hamming entre valorar y rarolav, es 4,
#pues hay 4 caracteres que difieren y solo las letras o y a, estan 
#en la misma posicion en ambos strings.



#Restricciones del problema: No se puede utilizar las palabras reservadas for e in


#Descripcion: Funcion que permite determinar distancia de hamming entre dos palabras
#Dom: palabra1, palabra2
#Rec: distancia hamming entre palabra1 y palabra2

def distancia_hamming(palabra1, palabra2):
    i = 0
    distancia = 0
    while(i < len(palabra1)):
        if(palabra1[i] != palabra2[i]):
            distancia = distancia + 1
        i = i + 1
    return distancia

#Ejecucion del programa
print(distancia_hamming("101101001", "101001111"))
print(distancia_hamming("tener", "Tener"))          
print(distancia_hamming("valorar", "rarolav")) 