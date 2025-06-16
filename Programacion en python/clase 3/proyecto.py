





#Como realizar un menu para un programa en python
opcion = 0
while opcion != 5:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    #Opcion 1 suma de numeros
    if opcion == 1:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es {resultado}")
    
    #Opcion 2 resta de numeros
    elif opcion == 2:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es {resultado}")
    
    #Opcion 3 multiplicacion de numeros
    elif opcion == 3:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es {resultado}")
    
    #Opcion 4 division de numeros
    elif opcion == 4:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"La división de {num1} entre {num2} es {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    
    #Opcion 5 salir del programa
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida, por favor seleccione una opción del menú.")