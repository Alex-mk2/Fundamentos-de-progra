# Crear un programa en Python que calcule las comisiones de venta mensuales
#basándose en las reglas de comisión proporcionadas. 

#Inicializar las variables
total_ventas = 0 #Acumulador para almacenar el total de ventas 
comision = 0
total_comision = 0 #acumulador
promedio = 0 
comision_mayor_300 = 0 #Contador
# Primero validamos que se ingrese la cantidad de meses
meses = 0 #Inicializar los meses para el ciclo
while meses <= 0:
    meses = int(input("Ingrese la cantidad de meses a evaluar: "))
    if meses <= 0:
        print("El número debe ser positivo. Intente nuevamente.")
# Se crea un iterador para que se recorra cada mes en el ciclo 
i = 0
#Se valida el total de ventas
while i < meses:
    total_ventas = float(input(f"Ingrese el total de ventas para el mes: "))
    if total_ventas < 0:
        print("El número debe ser no negativo. Intente nuevamente.")
    
    #Calcular la comision segun la tabla
    if(total_ventas < 500):
        print("No hay comisión")
    elif(500 <= total_ventas < 1000):
        comision = total_ventas * 0.05 
    elif(1000  <= total_ventas <= 5000):
        comision = total_ventas * 0.08
    else:
        comision = total_ventas * 0.10 + 200

    total_comision = total_comision + comision
    if(comision > 300):
        comision_mayor_300 = comision_mayor_300 + 1

promedio = total_comision/meses


#Mostrar resultados
print("Total acumulado de comisiones:", total_comision)
print("Promedio de comisión mensual:", promedio)
print("Meses con comisión > $300:", comision_mayor_300)