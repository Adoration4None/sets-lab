def unionConjuntos(sets):

    conjuntoUnion = set()

    # Iteramos sobre cada conjunto en el array
    for conjunto in set:
        # Iteramos sobre cada elemento del conjunto actual
        for elemento in conjunto:
            # Verificamos si el elemento no está presente en el conjunto resultado
            if elemento not in conjuntoUnion:
                conjuntoUnion.add(elemento)
    return conjuntoUnion