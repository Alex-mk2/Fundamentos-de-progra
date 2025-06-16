#Programa que solicite ingresar al usuario un numero por pantalla
# 1 debe imprimir la secuencia.........
# numero = 9------------->(0,1,2,3,4,5,6,7,8,9).....
# 2 contar cuantos de esos son multiplos de 3 y multiplos de 6 (sum = sum + 1)
# 3 calcular la suma de todos los numeros impares
# 4 mostrar por pantalla (print...)




#Se le pide un numero al usuario
numero = int(input("Ingrese un numero: "))

#Numero = 28...

#Se genera un iterador
i = 0

#i = 0

#Se genera la suma
suma = 0  #Suma de numeros impares .. 
mul_3 = 0 #Suma_Multiplos de 3 ..
mul_6 = 0 #Suma_multiplos de 6 .. 


#Mientras no alcance el numero ingresado
while(i <= numero): #0 <= 28...

    #Voy a contar los numeros que se ingresan
    #suma_numeros = suma_numeros + 1

    #Si el numero es multiplo de 3
    if(i % 3 == 0):
        mul_3 += 1
    
    #Si el numero es multiplo de 6
    if(i % 6 == 0):
        mul_6 += 1

    #Si el numero es impar
    if(i % 2 != 0):
        suma += i
    
    #Se imprime el numero
    print(i, end=",")

    #Se aumenta el iterador
    i += 1

#Reporte de resultados
print("\nLos multiplos de 3 son: ", mul_3)
print("\nLos multiplos de 6 son: ", mul_6)
print("\nLa suma de los numeros impares es: ", suma)




#Traza de la ejecucion
#i = 0
#numero = 28

#secuencia = (0 , 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
#18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28)

#mul_3 = (i % 3 == 0)---------->(0 % 3 == 0) = True
#mul_3 = (i % 3 == 0)---------->(3 % 3 == 0) = True
#mul_3 = (i % 3 == 0)---------->(5 % 3 == 0)---------> 5 % 3 = 1---------> 5 % 3 = 2 -------> falsa
#                                                      5 - 3 = 2

#mul_3 = (i % 3 == 0)---------->(6 % 3 == 0)---------> 6 % 3 = 2---------> 6 % 3 = 0--------> Verdadero
#                                                      6 - 6 = 0 

#suma_mul3 = 0 + 1 = 1 # mul_3 = 1
#suma_mul3 = 1 + 1 = 2 # mul_3 = 2
#suma_mul3 = 2 + 1 = 3 # mul_3 = 3
#mul_6 = (i % 6 == 0)



#Impares: (1,3,5,7...)


#Si un numero par debe cumplir que (i % 2 == 0)
#Un numero divisible por 2...

# (0 % 2) == True --------> (2N) numeros--------> 2 (N = 3)-----> 2 * 3 = 6 
# (2 % 2) == True
# (4 % 2) == True
# (6 % 2) == True
# (8 % 2) == True


#Impares siguen el siguiente comportamiento
#Para que un numero sea impar debe cumplir que (i % 2 != 0) a que sea cualquier numero menos el 0
#(1 % 2)-------> (1 % 2) = 0 ---------> (1 % 2) = 1
#                (1 - 0) = 1


#(3 % 2)-------> (3 % 2) = 1----------> (3 % 2) = 1
#                (3 - 2) = 1

#(5 % 2) ------> (5 % 2) = 2-----------> (5 % 2) = 1
#                (5 - 4) = 1


#.......------> Los impares se comportaran como (2N + 1) con N siendo numero positivo
#(2 * (3) + 1) = 7 impar
