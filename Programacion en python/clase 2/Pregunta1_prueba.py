
#Construya un programa que reciba un numero de 2 a 9 y muestre por pantalla
#Todos los numeros entre 1 y 100 que no sean multiplos del numero ingresado
#Ni que contengan un digito con ese mismo numero

#Ejemplo: Si el usuario ingresa 3, el programa debe mostrar los numeros:
#1 2 4 5 7 8 10 11 14 16 17 
#19 20 22 25 26 28 29 40 41 44 46 47 49 50 52 
#55 56 58 59 61 62 64 65 67 68 70 71 74 76 77 
#79 80 82 85 86 88 89 91 92 94 95 97 98 100


#Definicion de variables
#Entrada del usuario: Requiere de un numero entre 2 y 9
#Salida: Muestra los numeros entre 1 y 100 que no sean multiplos del numero ingresado ni que contengan un digito 
#con ese mismo numero

numero = int(input("Ingrese un numero entre 2 y 9: "))

#Se realiza la validacion del numero ingresado por el usuario
while(numero < 2 or numero > 9):
    numero = int(input("Numero invalido. Ingrese un numero entre 2 y 9: "))

    #Se crea un iterador
    i = 0

    #Mientras no alcance el largo de la lista
    while(i <= 100):
        #Si el numero recorrido no es multiplo del numero ingresado por el usuario
        if(i % numero != 0): #Si es distinto de 0, no va a ser multiplo
            #Si el numero no contiene el digito
            if(str(numero) not in str(i)):
                #Se imprime el numero
                print(i, end=", ")
        i+=1

#Multiplos del numero
#Traza: -----------> 3
#Interador = 0
#Condicion------>0 % 3 != 0 -------> 0%3 = 0------------> 0 != 0 == Falso
#Iterador = 1 
#Condicion------>1 % 3 != 0--------> 1%3 = 1------------> 1 != 0 == Verdadero
#Iterador = 2
#Condicion------>2 % 3 != 0--------> 2%3 = 2------------> 2 != 0 == Verdadero
#Iterador = 3
#Condicion------>3 % 3 != 0--------> 3%3 = 0------------> 0 != 0 == Falso


#Fin de la traza#

#Iterador = 9
#Condicion------> 9 % 3 != 0--------> 9%3 = 0 ------------> 0!= 0 == Falso



#Si en este caso el numero ingresado es el 5
#Iterador = 5
#Condicion------> 5 % 5 != 0--------> 5%5 = 0 ------------> 0!= 0 == Falso


#Iterador = 10
#Condicion------> 10 % 5 != 0 --------> 10 % 5 = 0 ------------> 0 != 0 == Falso

#"Dentro de la interpretacion del segundo condicional"
#if(str(numero) not in str(i))------------> "Si un numero en formato "string" no esta en el formato string (iterador)"

