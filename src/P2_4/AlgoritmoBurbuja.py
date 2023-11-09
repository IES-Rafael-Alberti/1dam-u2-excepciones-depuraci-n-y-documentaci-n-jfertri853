# Too easy
def ordenar_lista(lista: list) -> list:
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
    cadena = ""
    for i in range(0, len(lista)):
        if i == len(lista) - 1:
            cadena += str(lista[i])
        else:
            cadena += str(lista[i]) + ", "
    return cadena


def continuar():
    comando = input("Quieres introducir otro numero? (s/n): ").upper()
    if comando == "S":
        return True
    elif comando == "N":
        return False
    else:
        raise ValueError("Has introducido algo diferente a S o N")


def pedir_num() -> int:
    num = int(input("Introduce un numero: "))
    return num


def pedir_lista():
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
