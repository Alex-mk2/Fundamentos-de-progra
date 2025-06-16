#Se solicita al usuario que ingrese la altura inicial
altura_inicial = float(input("Ingrese la altura inicial de la pelota: "))

#Inicializar las variables
contador_rebotes = 0 # Contar cuantas veces golpea la pelota al suelo
distancia_total = 0 # Acumulador para saber cuanto fue la distancia de cada rebote
altura_max = altura_inicial # Se guardara la mayor altura alcanzada tras un rebote
rebote_max = 0 # Se guardará  el número de rebote en el que se alcanzó la mayor altura

#Se va contar desde la primera caída de la pelota desde la altura_inicial hasta el suelo antes del ciclo
distancia_total = distancia_total + altura_inicial

#Se le solicita al usuario ingresar el coeficiente de restitucion
r = float(input("Ingrese el coeficiente de restitución (entre 0 y 1): "))
# Mientras r esté fuera del rango (0,1), repetimos la solicitud
while(r <= 0 or r >= 1):
    print("Valor inválido. El coeficiente debe cumplir 0 < r < 1.")
    #Volvemos a pedir el valor hasta que el usuario ingrese algo en el rango permitido
    r = float(input("Por favor, ingresa nuevamente el coeficiente de restitución: "))

# Se crea el ciclo para el siguiente rebota si alcanze al menos 0.10
while(altura_inicial * r >= 0.10):
    #Formula para calcular la nueva_altura
    nueva_altura = altura_inicial * r 
    #Contador de rebotes se va incrementar
    contador_rebotes = contador_rebotes + 1
    #Se va sumar siempre subida + la bajada de la pelota
    distancia_total = distancia_total + nueva_altura * 2 

    # Se verifica si esta nueva altura es la mayor alcanzada hasta ahora
    if(nueva_altura > altura_max):
        altura_max = nueva_altura #Se actualiza el maximo
        rebote_max = contador_rebotes #Se actualiza el rebote max

    # Se actualiza la altura inicial para el siguiente rebote
    altura_inicial  = nueva_altura


#Mostrar resultados al usuario
# Mostrar resultados al usuario
print("Rebotes totales:", contador_rebotes)
print(f"Distancia total recorrida: {distancia_total:.2f} m")
print(f"Altura máxima: {altura_max:.2f} m (en rebote {rebote_max})")
