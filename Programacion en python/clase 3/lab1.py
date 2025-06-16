#Programa que calcula las comisiones de venta mensuales
#De acuerdo a las siguientes reglas:

#Ventas menos a 500 no hay comision
#Ventas entre 500 y 1000, comision del 5%
#Ventas entre 1000 y 5000, comision del 8%
#Ventas mayores a 5000, comision del 10% + 200


#Variables a utilizar por el programa


#Almacenar meses
meses = int(input("Ingrese la cantidad de meses a evaluar: "))


#Total ventas
total_ventas = 0

#Comision
comision = 0

#Total comision
total_comision = 0

#Promedio
promedio_comision = 0

#Contador de meses con comision mayor a 300
comision_mayor_300 = 0


#Se genera un contador
contador = 0

#Mientras no supere a los meses
while(contador < meses):
    #Validar meses...

    #Solicitar total de ventas
    total_ventas = float(input("Ingrese el total de ventas: "))

    #Validar que el total de ventas no sea negativo
    if (total_ventas < 0):
        print("El total de ventas no puede ser negativo. Intente nuevamente.")
        
    #De acuerdo a la siguiente tabla se calcula la comision

    if(total_ventas < 500):
        print("No hay comision")

    elif(500 <= total_ventas < 1000):
        comision = total_ventas * 0.05
    elif(1000  <= total_ventas <= 5000):
        comision = total_ventas * 0.08
    else:
        comision = total_ventas * 0.10 + 200
    
    #Se acumula la comision
    total_comision = total_comision + comision

    #Si la comision es mayor a 300
    if(comision > 300):
        comision_mayor_300 = comision_mayor_300 + 1
    
    #Se incrementa el contador
    contador = contador + 1


#Luego para calcular el promedio de las comisiones
promedio_comision = total_comision / meses

#Reporte del sistema#
print("Total acumulado de comisiones: ", total_comision)
print("Promedio de comision mensual: ", promedio_comision)
print("Meses con comision mayor a 300: ", comision_mayor_300)
