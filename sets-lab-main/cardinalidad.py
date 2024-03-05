def cardinalidadConjuntos(conjuntos):
    # Creamos un conjunto vacío para almacenar la unión de todos los conjuntos
    union = set()

    # Iteramos sobre cada conjunto en la lista
    for conjunto in conjuntos:
        # Agregamos todos los elementos del conjunto a la unión
        union.update(conjunto)

    # Devolvemos la cardinalidad de la unión
    return len(union)