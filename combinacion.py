# Función para calcular la combinación de conjuntos
def combinacionConjuntos(conjuntos):
    if len(conjuntos) < 2:
        return "Se requieren al menos dos conjuntos para calcular la combinación."

    # Creamos una lista para almacenar todas las combinaciones
    combinaciones = []

    # Obtenemos todas las combinaciones posibles de dos conjuntos
    for i in range(len(conjuntos)):
        for j in range(i + 1, len(conjuntos)):
            conjunto_i = conjuntos[i]
            conjunto_j = conjuntos[j]
            combinacion_temporal = set()

            # Agregamos los elementos de ambos conjuntos a la combinación temporal
            for elemento in conjunto_i:
                combinacion_temporal.add(elemento)
            for elemento in conjunto_j:
                combinacion_temporal.add(elemento)

            # Agregamos la combinación temporal a la lista de combinaciones
            combinaciones.append(combinacion_temporal)

    return combinaciones
