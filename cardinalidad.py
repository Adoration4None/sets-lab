def cardinalidadConjuntos(conjuntos):
    # Creamos una lista para almacenar la cardinalidad de cada conjunto
    cardinalidades = []

    # Iteramos sobre cada conjunto en la lista
    for conjunto in conjuntos:
        # Agregamos la cardinalidad del conjunto actual a la lista
        cardinalidades.append(len(conjunto))

    # Devolvemos la lista de cardinalidades de los conjuntos
    return cardinalidades