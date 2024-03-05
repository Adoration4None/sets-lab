def verificar_subconjunto(conjunto_elegido, conjunto_referencia, conjuntos):

    conjunto_elegido = conjuntos[conjunto_elegido]
    conjunto_referencia = conjuntos[conjunto_referencia]

    es_subconjunto = True
    for elemento in conjunto_elegido:
        if elemento not in conjunto_referencia:
            es_subconjunto = False
            break

    if es_subconjunto:
        return "El conjunto elegido es un subconjunto del conjunto de referencia."
    else:
        return "El conjunto elegido NO es un subconjunto del conjunto de referencia."