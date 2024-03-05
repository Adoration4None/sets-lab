def calcular_diferencia(sets, opciones):
    set1 = sets[opciones[0]]
    set2 = sets[opciones[1]]
    
    diferencia = [elemento for elemento in set1 if elemento not in set2]
    
    return diferencia
