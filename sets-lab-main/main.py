import cardinalidad
import Interseccion
import union

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
            conjunto = set(elementos)
            sets.append(conjunto)
    return sets

def show_entered_sets(sets):
    print("\nConjuntos creados:")
    for i, conjunto in enumerate(sets):
        print(f"Conjunto {i+1}: {conjunto}")

def main():
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
            operations_menu()
        elif option == 2:
            cardinalidad.cardinalidadConjuntos()
        elif option == 3:
            subset_operation.perform_subset_operation()
        elif option == 4:
            disjoint_operation.perform_disjoint_operation()
        elif option == 5:
            print("¡Hasta luego!")
        else:
            print("Opción no válida, por favor intente de nuevo.")

def operations_menu():
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
            union.unionConjuntos()
        elif option == 2:
            Interseccion.interseccionConjuntos()
        elif option == 3:
            difference_operation.perform_difference_operation()
        elif option == 4:
            complement_operation.perform_complement_operation()
        elif option == 5:
            combination_operation.perform_combination_operation()
        elif option == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()