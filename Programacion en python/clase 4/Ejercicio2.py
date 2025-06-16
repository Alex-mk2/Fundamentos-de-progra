#Agenda de contactos, se le solicita hacer lo siguiente:
# 1. Crear la estructura de agenda de contactos: debe tener nombre, telefono, correo
# 2. Crear un menu de opciones para el usuario
# 3. Crear una funcion para agregar un contacto
# 4. Crear una funcion para eliminar un contacto
# 5. Crear una funcion para buscar un contacto
# 6. Crear una funcion para mostrar todos los contactos
# 7. Crear una funcion que permita modificar el correo



#Se diseña la estructura de la agenda
agenda = {
    "Juan": {"Telefono": "93356723", "Correo": "juan@gmail.com"},
    "Ana": {"Telefono": "93356724", "Correo": "ana@gmail.com"},
    "Pedro": {"Telefono": "93356725", "Correo": "pedro@gmail.com"}         
}


#Descripcion: Funcion para agregar un contacto a la estructura agenda
#Dom: agenda X nombre X telefono X correo
#Rec: agenda actualizada con un nuevo contacto

def agregar_contacto(agenda, nombre, telefono, correo):
    agenda[nombre] = {"Telefono": telefono, "Correo": correo}
    return agenda


#Descripcion: Funcion para imprimir la agenda
#Dom: agenda
#Rec: Void

def imprimir_agenda(agenda):
    for nombre, datos in agenda.items():
        print(f"Nombre: {nombre}")
        print(f"Telefono: {datos['Telefono']}")
        print(f"Correo: {datos['Correo']}")
        print("-------------------------")

#Descripcion: Funcion para eliminar un contacto de la agenda
#Dom: agenda X nombre
#Rec: agenda actualizada sin el contacto eliminado

def eliminar_contacto(agenda, nombre):
    if(nombre in agenda):
        del agenda[nombre]
        print("Contacto eliminado...")
    return agenda


#Descripcion: Funcion para buscar un contacto en la agenda
#Dom: agenda X nombre
#Rec: agenda con el contacto a buscar

def buscar_contacto(agenda, nombre):
    if(nombre in agenda):
        print("El contacto buscado esta en la agenda")
    else:
        print("El contacto no se encuentra en la agenda")
    return agenda


#Descripcion: Funcion que permite modificar un contacto dentro de la agenda
#Dom: agenda X nombre 
#Rec: agenda con el contacto modificado

def modificar_nombre_contacto(agenda, nombre, nuevo_nombre):
    if(nombre in agenda):
        agenda[nuevo_nombre] = agenda[nombre]
        del agenda[nombre]
        print("Se ha modificado el contacto...")
    return agenda


#Descripcion: Funcion que permite modificar el correo de un contacto
#Dom: agenda X correo X nuevo_correo
#Rec: agenda con el nuevo correo

def modificar_correo(agenda, nombre, nuevo_correo):
    if nombre in agenda:
        if any(contacto["Correo"] == nuevo_correo for contacto in agenda.values()):
            print("Correo en uso...")

        else:
            agenda[nombre]["Correo"] = nuevo_correo
            print(f"Se ha modificado el correo de {nombre} a {nuevo_correo}")

    else:
        print("No esta en la agenda...")
    
    return agenda


        





#Menu de opciones para el usuario
opcion = 0
while (opcion != 6):
    print("Menu agenda de contactos")
    print("0. Imprimir la agenda")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Modificar contacto")
    print("5. Modificar correo")
    print("6. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if(opcion == 0):
        print("La agenda contiene:")
        imprimir_agenda(agenda)
    
    elif(opcion == 1):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        agenda = agregar_contacto(agenda, nombre, telefono, correo)
        print("Contacto agregado exitosamente.")
    
    elif(opcion == 2):
        nombre = input("Ingrese el nombre a eliminar: ")
        agenda = eliminar_contacto(agenda, nombre)

    elif(opcion == 3):
        nombre = input("Ingrese el nombre a buscar: ")
        agenda = buscar_contacto(agenda, nombre)
    
    elif(opcion == 4):
        nombre = input("Ingrese un nombre a buscar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del contacto: ")
        agenda = modificar_nombre_contacto(agenda, nombre, nuevo_nombre)
    
    elif(opcion == 5):
        nombre = input("Ingrese el nombre a buscar: ")
        nuevo_correo = input("Ingrese el nuevo correo: ")
        agenda = modificar_correo(agenda, nombre, nuevo_correo)

    elif(opcion == 6):
        print("Termino ejecucion...")
