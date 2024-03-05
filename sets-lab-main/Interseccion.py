def interseccionConjuntos(sets):
    # Verificamos si hay al menos un conjunto en la lista
    if not sets:
        return set()  # Si no hay conjuntos, la intersección es un conjunto vacío
    
    # Creamos un conjunto con los elementos del primer conjunto
    resultado = set(sets[0])

    # Iteramos sobre los conjuntos restantes en la lista
    for conjunto in sets[1:]:
        # Creamos un conjunto vacío para almacenar la intersección temporal
        interseccion_temporal = set()
        # Iteramos sobre cada elemento del conjunto actual
        for elemento in conjunto:
            # Si el elemento está presente en el resultado actual, lo agregamos a la intersección temporal
            if elemento in resultado:
                interseccion_temporal.add(elemento)
        # Actualizamos el resultado con la intersección temporal
        resultado = interseccion_temporal

    return resultado