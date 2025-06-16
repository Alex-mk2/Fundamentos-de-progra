#Pizza express (similar al ejercicio de taxis)

#Tarifa constante
tarifa = int(input("Ingrese la tarifa: "))

#Se asigna la tarifa a un costo inicial
costo_inicial = tarifa

#Se consulta los kilometros recorridos
kilometros = int(input("Ingrese los kilometros: "))

#Se genera el despacho 
despacho = 0

#Se genera cobros por km adicionales

#Se crea un iterador
if(tarifa <= 50):
    despacho = 8
    if(kilometros <= 3):
        despacho = 8
    else:
        despacho+=1.50

elif(tarifa >= 50 and tarifa < 100):
        despacho = 4
        if(kilometros <= 3):
            despacho = 4
        else:
            despacho+=1.00
    
else:
    despacho = 0
    if(kilometros <= 3):
         despacho = 0
    else:
         despacho+=0.75
        

print("El costo total es: ", costo_inicial + despacho)
print("El costo por kilometro es: ", despacho)


