#Ejercicio 2 parque de diversiones...




#Se le debe pedir al usuario edad y estatura en cm

edad = int(input("Ingrese su edad: "))
estatura = int(input("Ingrese su estatura en cm: "))

#De acuerdo a las siguientes condiciones


#edad < 12 #edad and estatura-------->#V and F = F
if(edad < 12 and estatura < 140):
    print("Solo juegos infantiles")

#Para juegos de adolescentes
elif((edad >= 12 and edad <= 17) and estatura > 0):
    print("Acceso a juegos de adolescentes")


#Si ya supera esa edad
elif(edad >= 18 and estatura >= 140):
    print("Acceso a todos los juegos")


#En el caso que no cumpla con la estatura
elif(estatura < 140 and edad > 0):
    print("No puede acceder a los juegos de alta intensidad")


