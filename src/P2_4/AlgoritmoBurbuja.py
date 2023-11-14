# Too easy
def ordenar_lista(lista: list) -> list:
    """Orders a list from lowest to highest

    Args:
        lista (list): A list composed by any type and any amount of values

    Returns:
        lista (list): lista but modified to be ordered from lowest to highest
    """
    total = len(lista) - 1
    intercambios = None
    contador = 0

    while contador != len(lista) and intercambios != 0:
        intercambios = 0

        for i in range(0, total):
            if lista[i] > lista[i + 1]:
                mayor = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = mayor
                intercambios += 1

        total -= 1
        contador += 1
    return lista


def mostrar_lista(lista: list) -> str:
    """Converts a list to a string in a format where values are separated by ","

    Args:
        lista (list): The list to convert to string and then format

    Returns:
        cadena (str): a string composed of the list elements separated by ", "
    """
    cadena = ""
    for i in range(0, len(lista)):
        if i == len(lista) - 1:
            cadena += str(lista[i])
        else:
            cadena += str(lista[i]) + ", "
    return cadena


def continuar():
    """Asks a yes or no question and returns True or False respectively

    Returns:
        True: when the input is "S" or "s"
        False: when the input is "N" or "n"

    """
    comando = input("Quieres introducir otro numero? (s/n): ").upper()
    if comando == "S":
        return True
    elif comando == "N":
        return False
    else:
        raise ValueError("Has introducido algo diferente a S o N")


def pedir_num() -> int:
    """Ask the user to input a numeric value and returns it as an integer

    Returns:
        num (int): the inserted numeric value
    """
    num = int(input("Introduce un numero: "))
    return num


def pedir_lista():
    """Returns a list of values based on user input

    Returns:
        lista (list): a list containing user inputs

    """
    lista = []
    seguir = True

    while seguir:
        try:
            num = pedir_num()
        except ValueError:
            print("*VALOR NO VALIDO* - se tomara como 0")
            num = 0

        lista.append(num)

        try:
            seguir = continuar()
        except ValueError as e:
            print("***ERROR*** -", e)
            seguir = False
    return lista


def main():
    lista1 = pedir_lista()
    listaOrdenada = ordenar_lista(lista1)
    print(mostrar_lista(listaOrdenada))


if __name__ == "__main__":
    main()
