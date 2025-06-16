# Diccionario del catálogo de libros por género
catalogo_libros = {
    "Ciencia Ficción": ["Dune", "Neuromante", "Fundación"],
    "Historia": ["Breve Historia del Tiempo", "Sapiens", "Historia de Roma"],
    "Autoayuda": ["El Poder del Ahora", "Hábitos Atómicos"]
}

# Diccionario de libros leídos por cada lector
libros_leidos = {
    "Ana": ["Dune", "Sapiens"],
    "Benjamín": ["Neuromante", "El Poder del Ahora", "Breve Historia del Tiempo"],
    "Claudia": ["Hábitos Atómicos", "Fundación", "Historia de Roma"]
}
# Descripción: Función para contar cuántos libros han sido leídos por género
# Dom: catalogo_libros X libros_leidos
# Rec: Cantidad de libros leídos por cada género
def contar_libros_por_genero(catalogo_libros, libros_leidos, nombre):
    contador_cf = 0
    contador_historia = 0
    contador_autoayuda = 0

    libros_por_persona = libros_leidos[nombre]

    for libro in libros_por_persona:
        if(libro in catalogo_libros["Ciencia Ficción"]):
            contador_cf = contador_cf + 1
        
        elif(libro in catalogo_libros["Historia"]):
            contador_historia = contador_historia + 1
        
        elif(libro in catalogo_libros["Autoayuda"]):
            contador_autoayuda = contador_autoayuda + 1
    
    
    print("---------------------Informe lecturas por nombre----------------------")
    print(f"Libros leidos por {nombre}")
    print(f"Topico ciencia ficcion: {contador_cf}")
    print(f"Topico auto-ayuda: {contador_autoayuda}")
    print(f"Topico historia: {contador_historia}")
    



#Descripcion: Funcion que permite recorrer todos los nombres del libro
#Dom: catalogo_libros X libros_leidos
#Rec: void

def contar_todos(catalogo_libros, libros_leidos):
    for nombre in libros_leidos:
        contar_libros_por_genero(catalogo_libros, libros_leidos, nombre)

#llamada al menu principal
contar_todos(catalogo_libros, libros_leidos)