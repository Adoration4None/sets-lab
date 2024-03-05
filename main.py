import cardinalidad, Interseccion, union, disjuntos, combinacion, diferencia, complemento, subconjunto

def get_number_of_sets():
    num_conjuntos = 0
    while num_conjuntos < 1 or num_conjuntos > 3:
        num_conjuntos = int(input("Ingrese el número de conjuntos que desea crear (máximo 3): "))
    return num_conjuntos

def creation_of_sets(number_of_sets):
    sets = []
    if number_of_sets > 1:
        for i in range(number_of_sets):
            elementos = input(f"Ingrese los elementos del conjunto {i+1} separados por comas: ").split(',')
            conjunto = set(elementos)
            sets.append(conjunto)
    return sets

def show_entered_sets(sets):
    print("\nConjuntos creados:")
    for i, conjunto in enumerate(sets):
        print(f"Conjunto {i+1}: {conjunto}")

def get_number_of_sets():
    num_conjuntos = 0
    while num_conjuntos < 1 or num_conjuntos > 3:
        num_conjuntos = int(input("Ingrese el número de conjuntos que desea crear (máximo 3): "))
    return num_conjuntos

def creation_of_sets(number_of_sets):
    sets = []
    if number_of_sets > 1:
        for i in range(number_of_sets):
            elementos = input(f"Ingrese los elementos del conjunto {i+1} separados por comas: ").split(',')
            conjunto = set(int(elemento) for elemento in elementos)
            sets.append(conjunto)
    return sets

def show_entered_sets(sets):
    print("\nConjuntos creados:")
    for i, conjunto in enumerate(sets):
        print(f"Conjunto {i+1}: {conjunto}")

def main():
    numberOfSets = get_number_of_sets()
    sets = creation_of_sets(numberOfSets)
    show_entered_sets(sets)

    option = 0
    while option != 5:
        print("\nMenu:")
        print("1. Operaciones entre 2 o 3 conjuntos")
        print("2. Cardinalidad")
        print("3. Subconjunto")
        print("4. Disjuntos")
        print("5. Salir")

        option = int(input("Ingrese su opción: "))
        if option == 1:
            operations_menu(sets)
        elif option == 2:
            print( f"Cardinalidad de los conjuntos: {cardinalidad.cardinalidadConjuntos(sets)}" )
        elif option == 3:
            elegido, referencia = -1, -1
            while elegido < 0 or elegido > len(sets):
                elegido = int( input("Que conjunto desea saber si es subconjunto de otro? [0/1/2]: ") )
            
            while referencia < 0 or referencia > len(sets):
                referencia = int( input("Cual sera ese otro conjunto de referencia? [0/1/2]: ") )

            print(f"{subconjunto.verificar_subconjunto(elegido, referencia, sets)}")
        elif option == 4:
            print( f"{disjuntos.disjuntos(sets)}" )
        elif option == 5:
            print("¡Hasta luego!")
        else:
            print("Opción no válida, por favor intente de nuevo.")

def operations_menu(sets):
    option = 0
    while option != 6:
        print("\nOperaciones entre conjuntos:")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Complemento")
        print("5. Combinación")
        print("6. Volver al menú principal")

        option = int(input("Ingrese su opción: "))
        if option == 1:
            print(f"Union: {union.unionConjuntos(sets)}")
        elif option == 2:
            interseccion = Interseccion.interseccionConjuntos(sets)
            if interseccion:
                print(f"Interseccion: {interseccion}")
            else: 
                print("Interseccion nula")
        elif option == 3:
            opcionesDiferencia = []
            while len(opcionesDiferencia) == 0:
                opcionesDiferencia = input("De que conjuntos desea conocer la diferencia? [0-1, 0-2, 1-0, 1-2, ...]: ").split('-')

            print(f"Diferencia: {diferencia.calcular_diferencia(sets, [int(opcion) for opcion in opcionesDiferencia])}")
        elif option == 4:
            opcionComplemento = -1
            while opcionComplemento < 0 or opcionComplemento > len(sets):
                opcionComplemento = int( input("De que conjunto desea conocer el complemento? [0/1/2]: ") )

            print(f"Complemento: {complemento.calcular_complemento(sets, opcionComplemento)[0]}")
            print(f"-calculado tomando como el universal: {complemento.calcular_complemento(sets, opcionComplemento)[1]}")
        elif option == 5:
            print(f"Combinacion: {combinacion.combinacionConjuntos(sets)}")
        elif option == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()