#Juan Oso ha incursionado en el increíble mundo del arriendo de quitasoles. 
#Para ello, ha cotizado en el mercado los diferentes tipos de auspiciadores 
#que puede conseguir y se ha decidido por uno: “Nibea”. 
#Este le reportará $200 pesos por cada día si compra sus quitasoles para arrendarlos, 
#con la promesa de un aumento del 4% por cada 5 quitasoles que tenga. 
#Juan Oso agrega quitasoles cada 3 días a razón de un 10% del total del día anterior.

#Si cada quitasol tiene un costo de $590, a Juan Oso le gustaría saber cuánto dinero
#puede obtener dada la cantidad de quitasoles que comprará en un inicio y el periodo,
#en días, en que los tendrá en arriendo.

#Variables del programa
quitasol = 590 #Precio por cada quitasol
ganancia = 200 #arriendo por cada quitasol
incremento = 0.04 #Solo se dara siempre y cuando tenga 5 quitasoles
dias_quitasoles = 3 #Son los quitasoles que se agregan cada 3 dias...
aumento_procentaje = 0.1 #Tendrá un aumento del 10% por el dia anterior

#El programa comienza con las siguientes variables al usuario
cantidad_quitasoles = int(input("Ingrese la cantidad de quitasoles: "))

#Los dias que espera tenerlos en arriendo (Por ejemplo: Arrendar por 7 dias o 3 dias o viceversa)
dias_arriendo = int(input("Ingrese la cantidad de dias que espera tenerlos en arriendo: "))

#Fin variables del usuario

#Ahora se contruye la lógica del programa

#Se inician la ganancia total
ganancia_total = 0 
inversion_total = cantidad_quitasoles * quitasol #Cant_quitasoles * quitasol--------> (3 * 590) = 1770

#Contador de quitasoles
i = 1

while(i <= dias_arriendo): #(3 <= 2)
    seccion_quitasoles = cantidad_quitasoles // 5 # "//" es una division entera o exacta...
    #Se calcula la ganancia por cada quitasol
    ganancia_por_quitasol = ganancia * (1 + incremento * seccion_quitasoles) #0.04 + 1 = 1.04


    #Ganancia por dia
    ganancia_dia = ganancia_por_quitasol * cantidad_quitasoles
    ganancia_total += ganancia_dia

    #Por cada tres dias (2 % 3)-----> 2 == 0?
    if i % dias_quitasoles == 0:
        cantidad_quitasoles += int(cantidad_quitasoles * aumento_procentaje)

    
    #Se aumentan los dias
    i = i + 1

ganancia_total = ganancia_total - inversion_total
print("La ganancia total es de: ", ganancia_total, " pesos")
print("La inversion total es de: ", inversion_total, " pesos")


#Traza que nos ilustra esto...
#Dias de arriendo = 2
#Cantidad de quitasoles = 3
#Ganancia_total = 0
#dias_quitasoles = 3
#Inversion_total = (590 * 3) = 1770
#dias = 1
#While------> Mientras que dias <= dias_arriendo...... 1 <= 2

#Seccion_quitasoles = (3 // 5) division entera o exacta-------> 0

#Ganancia_por_cada_uno_de_los_quitasoles = (200) * (1 + 0.04 * 0)) = (200) * (1) = 200
#Incremento = 0.04 * 100 = 4%
#Ganancia_del_dia = (3) * (200) = 600
#Ganancia_total = ganancia_total + ganancia_del_dia-------> (0) + (600) = 600


#Si (dias = 1) % (dias_quitasoles = 3) == 0-------> (1 % 3) == 1--------> 1 == 0? Falso
#dias = dias + 1

#Dias es igual a 2...
#Ganancia_total = ganancia_total + ganacia_del_dia-------> (600) + (600) = 1200

#Si (dias = 2) % (dias_quitasoles = 3)------> (2 % 3) = 2--------> 2 == 0? Falso
#Ganancia_total = 1200
#dias = dias + 1
#dias = 3


#Ganancia_total = ganancia_total - inversion_total = (1200 - 1770) = -570

