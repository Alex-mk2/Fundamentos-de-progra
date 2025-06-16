# Modelamiento de rebotes

#Entrada...
altura_inicial = float(input("Ingrese la altura inicial en metros: "))
coeficiente_restitucion = float(input("Ingrese el coeficiente de restitución (entre 0 y 1): "))

#Variables del sistema
altura_maxima = 0
rebote_maximo = 0
rebote_actual = 1
distancia_total = altura_inicial
nueva_altura = altura_inicial * coeficiente_restitucion

#Simulación
while nueva_altura >= 0.10:
    distancia_total += nueva_altura * 2
    if nueva_altura > altura_maxima:
        altura_maxima = nueva_altura
        rebote_maximo = rebote_actual + 1
    nueva_altura *= coeficiente_restitucion
    rebote_actual += 1

#Salida del programa...
print("\n--- Informe de rebotes ---")
print(f"Rebotes: {rebote_actual}")
print(f"Distancia total recorrida: {distancia_total:.2f} m")
print(f"Altura máxima: {altura_maxima:.2f} m (en el rebote {rebote_maximo})")


