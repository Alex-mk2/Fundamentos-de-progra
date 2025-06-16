#Juanito es un linguista que esta investigando las redundancias en el lenguaje, 
#para ello esta intentando reducir las
#palabras a su minima expresion, para ello ha consultado
#en sus referencias y un algoritmo que podrıa servirle es el de
#reduccion de strings, el cual es un algoritmo sencillo
#que funciona solo con un par de reglas:

#1-Se pueden eliminar cualquier par de letras adyacentes,siempre y cuando estas sean iguales
#2-Mientras existan dos letras iguales adyacentes, se deben seguir eliminando 
#los pares hasta que no quede ningun par de letras iguales adyacentes.

#Ejemplo primer caso:
#Si la entrada fuese ’aabcc’, 
#el resultado serıa 'b', 
#pues se pueden eliminar las ’aa’ del inicio y las ’cc’ del final.


#Ejemplo segundo caso: 
#Si la entrada fuese ’aaabccddd’, el resultado seria ’abd’

#'aaabccddd'---------> 'abccddd'-------->'abddd'-------->'abd'


#Construya un programa que permita la redución de palabras


#Descripcion: Funcion que permite la eliminacion/reducion de palabras
#Dom: palabra
#Rec: palabra reducida

def reducir_palabra(palabra): 
    lista = []
    #Se recorre cada letra en la palabra
    for letra in palabra:
        #Se busca las posiciones adyacentes (inicio-final)
        if(lista and lista[-1] == letra):
            #Se quita
            lista.pop()
        else:
            lista.append(letra)
    
    #Se concatena el resultado y se retorna
    return ''.join(lista)



#Pop es una funcion de listas que permite quitar elementos....

#Ejemplo de uso
print(reducir_palabra("aaabccddd"))  