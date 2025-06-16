#Johnny es un linguista estudiando como se utilizan las vocales en los distintos idiomas del mundo, 
#en particular, segunsu teoria, idiomas basados en el latin, como el espanol, italiano y frances tienden
# a tener mas palabras con vocales consecutivas, mientras que otras lenguas europeas 
#tienen menos palabras con vocales consecutivas. A fin de poder terminar su investigacion Johnny 
#necesita un metodo rapido de determinar la cantidad de vocales consecutivas dentro de una palabra,
#por lo que solicita a usted la construccion de un programa en Python que automatice el proceso, es decir, 
#se recibe como entrada un string y se entrega como respuesta el largo del substring que contenga mas
#vocales sin interrupciones, por ejemplo:
#*-Si la entrada fuese: ’groovy’, el substring mas largo de vocales es de largo 2, ’oo’
#*-Si la entrada fuese: ’oiseaux’, el substring mas largo de vocales es de largo 3, ’eau’
#*-Si la entrada fuese: ’hubschrauber’, el substring mas largo de vocales es de largo 2, ’au’
#Considere que su entrada siempre estar´a compuesta solamente por caracteres alfabeticos sin tilde
#y en minuscula. Para su solucion, no puede utilizar las palabras reservadas for e in.


#Restricciones: No se puede utilizar for e in



#Descripcion: Funcion que permite determinar si es una vocal
#Dom: letra
#Rec: cada vez que aparece una vocal devuelve True, caso contrario False

def es_vocal(letra):
    return letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"




#Descripcion: Funcion que permite encontrar el largo del substring con mas vocales consecutivas
#Dom: palabra
#Rec: largo del substring con mas vocales consecutivas

def vocales_consecutivas(palabra):
    largo = 0
    i = 0
    while(i < len(palabra)):
        if(es_vocal(palabra[i])):
            largo_actual = 1
            j = i + 1
            while(j < len(palabra) and es_vocal(palabra[j])):
                largo_actual += 1
                j = j + 1
            if(largo_actual > largo):
                largo = largo_actual
            i = j
        else:
            i+= 1
    return largo



#Ejecucion del programa
print(vocales_consecutivas("groovy"))       
print(vocales_consecutivas("oiseaux"))      
print(vocales_consecutivas("hubschrauber"))



