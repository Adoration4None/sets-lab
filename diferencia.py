def calcular_diferencia(sets):
    set1 = sets[0]
    set2 = sets[1]
    
    diferencia = [elemento for elemento in set1 if elemento not in set2]
    
    return diferencia
