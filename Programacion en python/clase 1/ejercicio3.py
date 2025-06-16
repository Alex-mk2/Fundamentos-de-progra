#Mismo ejercicio del semestre pasado...


#Solicitar por pantalla la cantidad de estudiantes
estudiantes = int(input("Ingrese numero total de estudiantes:"))


#Se crea un contador, para los aprobados y reprobados
contador_aprobados = 0
contador_reprobados = 0


#Contador de estudiantes
contador_estudiantes = 0


#Se crea un contador para la suma de calificaciones
suma_calificaciones = 0


#Nota maxima y minima
calificacion_maxima = 10
calificacion_minima = 70


#Mientras la calificación sea menor al numero total de estudianres
while(contador_estudiantes < estudiantes):
    calificacion = int(input("Ingrese una nota por estudiante:"))

    #Validacion del rango de notas
    if(10 <= calificacion <= 70):
        suma_calificaciones = suma_calificaciones + calificacion
        contador_estudiantes = contador_estudiantes + 1
        
        #Caso en que el estudiante aprubea
        if(calificacion >= 40):
            contador_aprobados = contador_aprobados + 1     

        #Caso en que el estudiante reprueba
        else:
            contador_reprobados = contador_reprobados + 1
        
        #Revision de nota mas alta y baja
        if(calificacion > calificacion_maxima):
            calificacion_maxima = calificacion
        if(calificacion < calificacion_minima):
            calificacion_minima = calificacion

    else:
        print("Calificación inválida. Debe estar entre 10 y 70.")


#Por ultimo se calcula el promedio de todas las notas ingresadas
promedio = suma_calificaciones/ estudiantes


#Imprimir los resultados
print("--------------------------#Resumen de notas de los estudiantes#---------------------------")
print("Calificación más alta:", calificacion_maxima)
print("Calificación más baja:", calificacion_minima)
print("Promedio de notas:", promedio)
print("Número de estudiantes aprobados:", contador_aprobados)
print("Número de estudiantes reprobados:", contador_reprobados)