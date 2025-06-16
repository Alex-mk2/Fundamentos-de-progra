#Ejercicio 2 "climaHoy", similar al ejercicio promedios de temperaturas


#Se crea un contador y variables para las temperaturas
contador_temp = 0
alta = 0
moderado = 0
baja = 0


#Se crea variables para obtener minimo y maximo de temperaturas
temp_min = 101
temp_max = -1


#Se crea una variable para la suma de temperaturas
suma_temperaturas = 0


#Se le solicita al usuario cantidad de temperaturas
cant_temperaturas = int(input("Ingrese la cantidad dias de temperaturas: "))


#Mientras contador no supere a cant_temperaturas
while(contador_temp < cant_temperaturas):

    #Ingresar las temperaturas
    temperatura = int(input("Ingrese la temperatura:"))

    #Se realiza la suma de temperaturas:
    suma_temperaturas += temperatura

    #Se crean las condiciones
    if(temperatura >= 30):
        alta += 1
    elif(temperatura >= 15 and temperatura < 30):
        moderado += 1
    elif(temperatura < 15):
        baja += 1
    else:
        print("Temperatura no válida")

    
    #Se genera la condicion para buscar temperatura baja y alta
    if(temperatura > temp_max):
        temp_max = temperatura
    if(temperatura < temp_min):
        temp_min = temperatura

    #Se incrementa el contador 
    contador_temp += 1


#Se obtiene el promedio de las temperaturas
promedio = suma_temperaturas / cant_temperaturas 


#Se imprimen los resultados de las temperaturas
print("################-Reporte de temperaturas-#################:")
print("Temperaturas altas:", alta)
print("Temperaturas moderadas:", moderado)
print("Temperaturas bajas:", baja)
print("Promedio de temperaturas:", promedio)
print("Temperatura máxima:", temp_max)
print("Temperatura mínima:", temp_min)


