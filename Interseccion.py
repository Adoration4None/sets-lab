def interseccionConjuntos(sets):
    
    # Creamos un conjunto con los elementos del primer conjunto
    resultado = set(sets[0])
    intersecciones = []

    # Iteramos sobre los conjuntos restantes en la lista
    for i, conjunto in enumerate(sets[1:], start=1):
        # Creamos un conjunto vacío para almacenar la intersección temporal
        interseccion_temporal = set()
        # Iteramos sobre cada elemento del conjunto actual
        for elemento in conjunto:
            # Si el elemento está presente en el resultado actual, lo agregamos a la intersección temporal
            if elemento in resultado:
                interseccion_temporal.add(elemento)
        if interseccion_temporal == set():
            intersecciones.append((f"Conjunto 1 y Conjunto {i+1}: No hay intersección"))    
        else:
            # Guardamos la intersección entre el primer conjunto y el conjunto actual
            intersecciones.append((f"Conjunto 1 y Conjunto {i+1}: {interseccion_temporal}"))    

    if len(sets) > 2:
        conjunto2 = sets[1]
        conjunto3 = sets[2]
        interseccion_temporal = set()
        # Iteramos sobre cada elemento del conjunto 2
        for elemento in conjunto2:
            # Si el elemento está presente en el conjunto 3, lo agregamos a la intersección temporal
            if elemento in conjunto3:
                interseccion_temporal.add(elemento)
        
        if not interseccion_temporal:
            intersecciones.append(("Conjunto 2 y Conjunto 3: No hay intersección"))
        else:
            intersecciones.append(("Conjunto 2 y Conjunto 3:", interseccion_temporal))

        # Calcular la intersección entre todos los conjuntos
        interseccion_total = set(resultado)

        for conjunto in sets[1:]:
            interseccion_temporal = set()
            for elemento in interseccion_total:
                if elemento in conjunto:
                    interseccion_temporal.add(elemento)
            interseccion_total = interseccion_temporal

        if interseccion_temporal == set():
            intersecciones.append("Intersección de los 3 conjuntos: No hay intersección")    
        else:
            intersecciones.append((f"Intersección de los 3 conjuntos: {interseccion_total}"))

    return intersecciones