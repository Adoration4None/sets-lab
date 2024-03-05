def calcular_complemento(sets, opcion):
    conjunto = sets[opcion]
    
    conjunto_universal = generar_conjunto_universal(sets)
    
    complemento = [elemento for elemento in conjunto_universal if elemento not in conjunto]
    
    return complemento, conjunto_universal
    

def generar_conjunto_universal(sets):
    minimo = min(min(sets[0]), min(sets[1]))
    maximo = max(max(sets[0]), max(sets[1]))

    if len(sets) > 2:
        minimo = min(minimo, min(sets[2]))
        maximo = max(maximo, max(sets[2]))
    
    conjunto_universal = list(range(minimo, maximo + 1))
    
    return conjunto_universal