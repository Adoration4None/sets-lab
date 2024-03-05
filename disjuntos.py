def disjuntos(conjuntos):
    # Iteramos sobre todos los pares de conjuntos
    for i in range(len(conjuntos)):
        for j in range(i + 1, len(conjuntos)):
            conjunto1 = conjuntos[i]
            conjunto2 = conjuntos[j]
            # Verificar si algún elemento del conjunto 1 está presente en el conjunto 2
            for elemento in conjunto1:
                if elemento in conjunto2:
                    return "Los conjuntos no son disjuntos"

            return "Los conjuntos son disjuntos"
                    
