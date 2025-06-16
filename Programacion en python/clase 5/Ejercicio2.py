#La empresa TI-Fast, dedicada a soluciones tecnológicas, ha detectado múltiples 
#intentos de acceso no autorizado a su sistema interno.
#Por esta razón, el área de informática ha decidido 
#reforzar el sistema de autenticación del personal.
#Se requiere las siguientes funcionalidades:
#1-Genere un diccionario para almacenar usuario y contraseña asociado
#2-Implementar una funcion que permita encriptar una contraseña
#3-Implementar una funcion que permita encriptar un usuario
#4-Mostrar los usuarios y contraseñas encriptados


usuarios_ti_fast = {
    "juan.perez": "clave132", #usuario-contraseña
    "ana.gomez": "robotx",
    "benja.garrido": "root"
}


#Descripcion: Funcion que permite encriptar una contraseña
#Dom: clave (contraseña)
#Rec: clave encriptada (contraseña)

def encriptar_clave(clave):
    reemplazo_por = {'a': '@',
                     'e': '3',
                     'i': '1',
                     'o': '0', 
                     'u': 'ü',
                     'x': '.',
                     't': '*'}
    


    clave_a_invertir = clave[::-1] 
    #-> [::-1]-------> (se toma desde el inicio hasta el final)
    #Y se invierte la lista...

    #Se genera la clave encriptada
    clave_encriptada = ''.join(reemplazo_por.get(letra, letra) for letra in clave_a_invertir)
    return clave_encriptada


#clave132-----(Invertir string)------> "231evalc"
#Remplazo----(Encriptacion)-------> "2313v@lc"
# fruta = "pera"
# frutab = "manzana"
# frutac-----> join()-------> "pera", "manzana"

#




#Descripcion: Funcion que permite encriptar a un usuario
#Dom: usuario
#Rec: usuario encriptado

def encriptar_usuario(usuario):
    separar_usuario = usuario.split(".")
    usuario_encriptado = [parte[0] + "*" * (len(parte) - 1) for parte in separar_usuario]
    return ''.join(usuario_encriptado)

#Join lo que realiza es concatenar dos o mas strings en uno solo...
#"a", "e", "i", "o", "u".join()---------> "aeiou"
#Split: Separa un string en distintos substrings "aeiou".split()-------> "a", "e", "i", "o", "u"



#Descripcion: Funcion que permite mostrar las claves y usuarios encriptados
#Dom: usuarios
#Rec: void

def mostrar_encriptacion(usuarios):
    print("Usuarios encriptados")
    for usuario, clave in usuarios.items():
         print(f"Usuario: {encriptar_usuario(usuario)} | Clave: {encriptar_clave(clave)}")



#Menu principal
mostrar_encriptacion(usuarios_ti_fast)