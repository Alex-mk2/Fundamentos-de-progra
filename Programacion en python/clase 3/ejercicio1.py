
#Ejercicio 1
#El usuario debe ingresar 3 numeros 
# un entero (int)-----> N (naturales)
# un real (float)-----> R (reales)
# un string (str)-----> "8".

#Inicio programa

#primer numero (entero)...
numero1 = int(input("Ingrese un numero entero: "))

#segundo numero (real)...
numero2 = float(input("Ingrese un numero real: "))

#tercer numero (str)... "8" o '8'
numero3 = str(input("Ingrese un numero en string: "))

#Se debe convertir el numero string a entero (int)...
numero3 = int(numero3) # '8' ----> 8 (int)

#Ahora bien, lo esencial del programa...

#Se debe sumar los tres numeros #Poder completar el primer inciso
suma = numero1 + numero2 + numero3 #Sumar los tres numeros

#numero1 = 5
#numero2 = 2.8
#numero3 = '3'-----> 3 (int)


#Anteriormente se menciono que el promedio es la suma de los numeros / cantidad de los numeros
#Para los numeros que tenemos ahora
#promedio = (numero1 + numero2 + numero3) / 3
#promedio = (5 + 2.8 + 3) / 3 --------> 3.6 (primer inciso)



#Lo primero que pregunta el programa, es el promedio de los 3 numeros
promedio = suma / 3
print("El promedio de los 3 numeros es: ", promedio)


#Segundo inciso

#Lo segundo, buscar mayor y menor
mayor = -1 #Esto es mas que nada por convencion... ("inf")
menor = 101 #Esto es mas que nada por convencion... ("sup")


#Logica para buscar numero mayor
#Patron... 


#Se traduce de la siguiente forma
#numero1 = 5
#5 > -1 y 5 > 2.8 y 5 > 3---------------> and ------> y ---------> 0 and 1 = F ----------> logica proposional------> p y q
#                                                                  1 and 1 = V
#                                                                  0 and 0 = V
#                                                                  1 and 0 = F

#  V    and      V     and      V -----------> V     
#5 > -1 and 5 > 2.8 and 5 > 3   ------->

#Recta numerica: (0...1...2...3...4...5) punto inicial = 0 

if(numero1 > mayor and numero1 > numero2 and numero1 > numero3):
    mayor = numero1 # 5


#numero2 = 2.8

#   V     and       F    and       F ---------> F
#2.8 > -1 and 2.8 > 5 and 2.8 > 3

#Condicion es falsa
elif(numero2 > mayor and numero2 > numero1 and numero2 > numero3):
    mayor = numero2


#numero3 = 3


#En cuanto al orden de los numeros
#numero1 = 5 (mayor)...

#             V    and   F   and   V ---------> "F"
#Condicion: 3 > -1 and 3 > 5 and 3 > 2.8
elif(numero3 > mayor and numero3 > numero1 and numero3 > numero2):
    mayor = numero3





#Logica para buscar numero menor
if(numero1 < menor and numero1 < numero2 and numero1 < numero3):
    menor = numero1
elif(numero2 < menor and numero2 < numero1 and numero2 < numero3):
    menor = numero2
elif(numero3 < menor and numero3 < numero1 and numero3 < numero2):
    menor = numero3

#Se imprime el resultado de mayor y menor
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)



#Solo numero1 y numero3 cumplen con esta condicion debido a que son enteros...

#Numero divisible por 3 y 5
#Un ejemplo es el 225... 225 / 3 = 75 y 225 / 5 = 45

#  numero1 and numero1 ---------> V and V = V
#                      ---------> F and V = F
if(numero1 % 3 == 0 and numero1 % 5 == 0):
    print("El numero ", numero1, " es divisible por 3 y 5")
