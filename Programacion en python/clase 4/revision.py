

#Catalogo de libros
#El contexto del problema aborda una libreria para la utilizacion de libros

#Se crea un diccionario para el catalogo de libros 

#Catálogo de la “biblioteca”
catalogo_libros = { "Ciencia Ficción": ["Dune", "Neuromante", "Fundación"],
    "Historia": ["Breve Historia del Tiempo", "Sapiens", "Historia de Roma"],
    "Autoayuda": ["El Poder del Ahora", "Hábitos Atómicos"] 
}


#Libros leidos
libros_leidos = { 
    "Ana": ["Dune", "Sapiens"],
    "Benjamín": ["Neuromante", "El Poder del Ahora", "Breve Historia del Tiempo"],
    "Claudia":  ["Hábitos Atómicos", "Fundación", "Historia de Roma"]
}


#Se busca saber cuantos libros completados pertenecen a cada genero...

#Descripcion: Funcion que permite contar que libros fueron leidos y a que genero pertenecen
#Dom: catalogo X libros_leidos X nombre
#Rec: contador con los libros que pertenecen a dicho genero

def pertenecen_genero_libros(catalogo, libros_leidos, nombre):
    contador = 0;
    libro_genero = {}

    #Se recorre cada genero
    for genero, libros in catalogo.items():
        for libro in libros:
            libro_genero[libro] = genero
    
    #Se cuenta el genero del libro
    contador_genero = {}

    for libro in libros_leidos[nombre]:
        genero = libro_genero.get(libro)
        if(genero):
            contador_genero[genero] = contador_genero.get(genero, 0) + 1
    
    return contador_genero



#Menu principal
print("Los libros que pertenecen a dicho genero son: ", pertenecen_genero_libros(catalogo_libros, libros_leidos, "Claudia"))




