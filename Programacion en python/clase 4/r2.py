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
def contar_libros_por_genero(catalogo_libros, libros_leidos):
    contador_cf = 0
    contador_historia = 0
    contador_autoayuda = 0

 # Se recorre el diccionario de lecturas (por cada lector)
    for lector in libros_leidos:
        # Se recorren los libros que cada lector ha leído
        for libro in libros_leidos[lector]:
            # Se verifica en qué género está el libro y se incrementa el contador correspondiente
            if libro in catalogo_libros["Ciencia Ficción"]:
                contador_cf = contador_cf + 1
            elif libro in catalogo_libros["Historia"]:
                contador_historia = contador_historia + 1
            elif libro in catalogo_libros["Autoayuda"]:
                contador_autoayuda = contador_autoayuda + 1

    # Se imprime el total de libros leídos por género
    print("Libros de Ciencia Ficción leídos:", contador_cf)
    print("Libros de Historia leídos:", contador_historia)
    print("Libros de Autoayuda leídos:", contador_autoayuda)



#ejecucion
contar_libros_por_genero(catalogo_libros, libros_leidos)