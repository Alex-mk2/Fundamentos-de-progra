
#Con diccionarios construye un programa que permita la gestion de notas de 
#estudiantes, lo cual debe hacer lo siguiente
#Todo tipo de dato: int X string X float X list X booleano
#Es que tienen diferentes funciones para acceder a ellos
#Diccionario-----------> elemento (estudiantes) X key (notas)------> valor (float) 
#laboratorio-----------> elemento (caballo) X key (velocidad_base), (prob_lesion), posicion (valor)
#nota1 = float(input("Ingrese tal cosa: "))
#nombre = input("Ingrese tal nombre")

#vaso = {"tipo_liquido", "cantidad_mil"}----------> recibe lo que se quiera...
#Importante: ¡Es que son mutables!---------> son modificables porque se puede acceder a
#Sus componentes... 

#Se puede modificar los datos como "tipo_liquido" y "cantidad_mil"
#Con diccionarios se puede---------> modificar, agregar, eliminar, crear
#CRUD----------> (create, read, update, delete)----> es importante que sean mutables
#Se les pide actualizar la velocidad del caballo------> operacion de update
#Personalizacion--------> nombre-------> create

#Es que pueden ser accedidos a traves de operadores--------> (del)-----> eliminar
#pop---------> (Es tomar el primer elemento del jenga---------> el primer bloque que esta en lo mas alto...)
#Operadores para acceder a sus elementos-----> items().

# 1: Obtener el promedio de los estudiantes (suma de las notas / cantidad notas)------> promedio (curso)
# 2: Obtener el mejor estudiante (mejor promedio > al resto de promedios)
# 3: Obtener los estudiantes aprobados (Condicion promedio notas >= 4.0)
# 4: Obtener los estudiantes reprobados(Condicion promedio notas < 4.0)
# 5: Construya un menu para el usuario y cree una funcion para imprimir el diccionario (mostrar el contenido del dic)
#Pero tambien darle al usuario opciones (opcion 1 = calcule prom), (opcion 2 = muestre por pantalla)
# 6: Construya una funcion que permita cambiar una nota de un estudiante(Juan : (5.0, 4.0, 3.5)--->update---->(5.0, 4.0, 4.0))
# 7: Construya una funcion que permita agregar un estudiante al diccionario (Alex : (4.5, 4.0, 3.2)------> create------> (Alex: (4.5, 4.0, 3.2)))
# 8: Construya una funcion que permita eliminar a un estudiante del diccionario (Alex : (4.5, 4.0, 3.2)-----> delete-----> []----> diccionario se actualiza)
# 9: Construya una funcion que permita cambiar el nombre de un estudiante (Juan : (5.0, 4.0, 3.5)-------> update-----> Roberto: (5.0, 4.0, 3.5)



#Se crea un diccionario con los estudiantes y sus respectivas notas
#Un diccionario puede aceptar cualquier tipo de dato...
#enteros X floantes X listas X strings

notas_estudiantes = {
    "Juan": [7.0, 4.0, 5.5], #estudiante---------> "nombre"
    "Pedro": [5.5, 2.5, 3.0],
    "Roberto": [2.0, 3.0, 3.5],
    "Maria": [5.5, 4.5, 4.0]
}

#Estructura que debe estar si o si...

#Descripcion: Funcion que permite el calculo de promedio de los estudiantes (Los que estan en el diccionario)
#Dom: Diccionario (argumento o paramentro de la funcion)------> lo que la funcion recibe
#Rec: promedio de notas de los estudiantes (promedio = (suma de las notas) / cantidad(notas)) (entero o flotante)------> floante
#-*Comentarios#

#item------> valor-----> key------->elemento


def promedio_estudiantes(diccionario):
    suma = 0
    cantidad = 0
    for estudiante, notas in diccionario.items():
        suma += sum(notas)
        cantidad += len(notas)
        promedio = suma / cantidad
    return promedio




#Descripcion: Funcion que permite obtener el mejor estudiante
#Dom: diccionario
#Rec: nombre del mejor estudiante X prom del mejor estudiante

def mejor_estudiante(diccionario):
    mejor = [] #
    mejor_promedio = 0
    for estudiante, notas in diccionario.items():
        promedio = sum(notas) / len(notas)
        if promedio > mejor_promedio:
            mejor_promedio = promedio #valor------>[7.0, 7.0, 7.0]
            mejor = estudiante #------->nombre asociado a ese promedio...
    return mejor, mejor_promedio



#Descripcion: Funcion que permite obtener los estudiantes aprobados
#Dom: diccionario
#Rec: lista de estudiantes aprobados

def estudiante_aprobado(diccionario):
    aprobados = []
    for estudiante, notas in diccionario.items():
        promedio = sum(notas) / len(notas)
        if(promedio >= 4.0):
            aprobados.append(estudiante)
    return aprobados


#Descripcion: Funcion que permite obtener los estudiantes reprobados
#Dom: diccionario
#Rec: lista de estudiantes reprobados

def estudiante_reprobado(diccionario):
    reprobados = []
    for estudiante, notas in diccionario.items(): #-----> nombre---------> lista[notas]
        promedio = sum(notas) / len(notas)
        if(promedio < 4.0):
            reprobados.append(estudiante)
    return reprobados


#Descripcion: Funcion para imprimir el contenido del diccionario
#Dom: diccionario
#Rec: Void

def imprimir_diccionario(diccionario):
    for estudiante, notas in diccionario.items():
        print(estudiante, ":", notas)


#Descripcion: Funcion que permite agregar la nota de un estudiante
#Dom: Diccionario, estudiante, nota
#Rec: diccionario

#diccionario--------> "nombre estudiante" [lista[notas]]
#agregando un elemento------->creando
def agregar_nota(diccionario, estudiante, nota):
    if(estudiante not in diccionario):
        diccionario[estudiante] = []
    diccionario[estudiante].append(nota) #le estamos creando una nota más...
    return diccionario


#Descripcion: Funcion que permite cambiar la nota de un estudiante
#Dom: Diccionario, estudiante, nota, indice
#Rec: diccionario

def cambiar_nota(diccionario, estudiante, nota, indice):
    if(estudiante in diccionario):
        notas = diccionario[estudiante]
        if(0 <= indice < len(notas)):
            notas[indice] = nota
    return diccionario

#Descripcion: Funcion que permite cambiar el nombre de un estudiante
#Dom: Diccionario, estudiante, nuevo nombre
#Rec: diccionario


#Libro de clases--------> Juan perez
#Error de nombre de un estudiante---------> dicho estudiante no se llama Juan perez
#Dicho estudiante se llama Roberto perez
#Que se debe hacer? Subrayar con corrector el nombre y cambiarlo
#Modificar un registro asociado al libro de clases

def cambiar_nombre(diccionario, estudiante, nuevo_nombre):
    if(estudiante in diccionario):
        diccionario[nuevo_nombre] = diccionario[estudiante]
        del diccionario[estudiante] #del--------> delete (Libro de clases------> corrector al nombre)
        #update---------> se actualiza libro de clases
    return diccionario

#Descripcion: Funcion que permite eliminar a un estudiante del diccionario
#Dom: Diccionario, estudiante
#Rec: diccionario

def eliminar_estudiante(diccionario, estudiante):
    if(estudiante in diccionario): #Debemos borrarlo------->otro libro de clases
        del diccionario[estudiante] #Delete o borrar
    return diccionario

#Descripcion: Funcion que permite agregar un estudiante al diccionario
#Dom: Diccionario X estudiante X nota
#Rec: diccionario

def agregar_estudiante(diccionario, estudiante, nota):
    if(estudiante not in diccionario):
        if(isinstance(nota, list)): #7.0-----------> al menos 4 notas------->Lista[nota1, nota2, nota3, nota4]
            diccionario[estudiante] = nota
    return diccionario #Create o crear

    


#*****************************Se construye un menu para el usuario para que utilice las opciones*********************#
opcion = 0
while(opcion != 10):
    print("Menu de opciones")
    print("0. Imprimir el diccionario")
    print("1. Obtener el promedio de los estudiantes")
    print("2. Obtener el mejor estudiante")
    print("3. Obtener los estudiantes aprobados")
    print("4. Obtener los estudiantes reprobados")
    print("5. Agregar la nota de un estudiante")
    print("6. Cambiar la nota de un estudiante")
    print("7. Eliminar a un estudiante")
    print("8. Agregar un estudiante")
    print("9. Cambiar el nombre de un estudiante")
    print("10. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if(opcion == 0):
        print("El diccionario contiene:")
        imprimir_diccionario(notas_estudiantes)
    
    elif(opcion == 1):
        print("El promedio de los estudiantes es: ", promedio_estudiantes(notas_estudiantes))

    elif(opcion == 2):
        mejor, mejor_promedio = mejor_estudiante(notas_estudiantes)
        print("El mejor estudiante es: ", mejor, "con un promedio de: ", mejor_promedio)

    elif(opcion == 3):
        print("Los estudiantes aprobados son: ", estudiante_aprobado(notas_estudiantes))

    elif(opcion == 4):
        print("Los estudiantes reprobados son: ", estudiante_reprobado(notas_estudiantes))
    
    elif(opcion == 5):
        estudiante = input("Ingrese nombre del estudiante: ")
        nota = float(input("Ingrese nota que desea agregar: "))
        agregar_nota(notas_estudiantes, estudiante, nota)
        print("Se ha agregado la nota del estudiante: ", estudiante, "a: ", nota)
    
    elif(opcion == 6):
        estudiante = input("Ingrese nombre del estudiante: ")
        indice = int(input("Ingrese la nota que desea cambiar (indice): "))
        nota = float(input("Ingrese la nueva nota: "))
        cambiar_nota(notas_estudiantes, estudiante, nota, indice)
        print("Se ha cambiado la nota del estudiante: ", estudiante, "a: ", nota)
    
    elif(opcion == 7):
        estudiante = input("Ingrese nombre del estudiante: ")
        eliminar_estudiante(notas_estudiantes, estudiante)
        print("Se ha eliminado al estudiante: ", estudiante)
    
    elif(opcion == 8):
        estudiante = input("Ingrese nombre del estudiante: ")
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
        notas = [nota1, nota2, nota3]
        agregar_estudiante(notas_estudiantes, estudiante, notas)
        print("Se ha agregado al estudiante: ", estudiante, "con las notas: ", notas)
    
    elif(opcion == 9):
        estudiante = input("Ingrese nombre del estudiante: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
        cambiar_nombre(notas_estudiantes, estudiante, nuevo_nombre)
        print("Se ha cambiado el nombre del estudiante: ", estudiante, "a: ", nuevo_nombre)
    
    elif(opcion == 10):
        print("Se termina el programa")



