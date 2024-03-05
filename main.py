#Pedir al usuario el número de conjuntos
def getNumberOfSets ():
    num_conjuntos = 0
    
    while(num_conjuntos < 1 or num_conjuntos > 3):
        num_conjuntos = int(input("Ingrese el número de conjuntos que desea crear (máximo 3): "))
    
    return num_conjuntos

#Proceso de creación de los conjuntos
def creationOfSets ( numberOfSets ):
    sets = []
    if numberOfSets > 1:
        for i in range (numberOfSets):
            # Solicitar al usuario que ingrese los conjuntos separados por comas
            elementos = input(f"Ingrese los elementos del conjunto {i+1} separados por comas: ").split(',')
            
            # Convertir la lista de elementos a un conjunto
            conjunto = set(elementos)
            
            #Añadir el conjunto a la lista de conjuntos
            sets.append(conjunto)
            
        return sets

def showEnteredSets(sets):
    #Imprimir los conjuntos con su contenido
    print("\nConjuntos creados:")
    for i, set in enumerate(sets):
        print(f"Conjunto {i+1}: {set}")

def start():
    numberOfSets = getNumberOfSets()
    sets = creationOfSets(numberOfSets)
    showEnteredSets(sets)
    
start()